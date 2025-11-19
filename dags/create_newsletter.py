import os

from airflow.models import DagRun
from airflow.sdk import asset, Asset, Metadata, ObjectStoragePath

# set these environment variables to store the newsletter
# in cloud object storage instead of the local filesystem
OBJECT_STORAGE_SYSTEM = os.getenv("OBJECT_STORAGE_SYSTEM", default="file")
OBJECT_STORAGE_CONN_ID = os.getenv("OBJECT_STORAGE_CONN_ID", default=None)
OBJECT_STORAGE_PATH_NEWSLETTER = os.getenv(
    "OBJECT_STORAGE_PATH_NEWSLETTER",
    default="include/newsletter",
)


def _get_run_date(triggering_asset: Asset = None, **context: dict) -> str | None:
    from datetime import datetime
    dag_run: DagRun = context.get("dag_run")

    if not dag_run:
        return None

    if triggering_asset and dag_run.run_type == "asset_triggered":
        asset_event = context["triggering_asset_events"][triggering_asset][0]
        return asset_event.extra["run_date"]
    elif getattr(dag_run, "logical_date", None):
        return dag_run.logical_date.strftime("%Y-%m-%d")
    else:
        return datetime.now().strftime("%Y-%m-%d")


@asset(schedule="@daily")
def raw_zen_quotes(context: dict):
    """
    Extracts a random set of quotes.
    """
    import requests

    r = requests.get("https://zenquotes.io/api/quotes/random")
    quotes = r.json()

    # always have a run date to know for which date the newsletter has been created
    run_date = _get_run_date(context=context)

    # attach the run date to the asset event
    yield Metadata(Asset("raw_zen_quotes"), {"run_date": run_date})

    return quotes


@asset(schedule=[raw_zen_quotes])
def selected_quotes(context: dict):
    """
    Transforms the extracted raw quotes.
    """
    import numpy as np

    raw_quotes = context["ti"].xcom_pull(
        dag_id="raw_zen_quotes",
        task_ids=["raw_zen_quotes"],
        key="return_value",
        include_prior_dates=True,
    )[0]

    quotes_character_counts = [int(quote["c"]) for quote in raw_quotes]
    median = np.median(quotes_character_counts)

    median_quote = min(
        raw_quotes,
        key=lambda quote: abs(int(quote["c"]) - median),
    )
    raw_quotes.pop(raw_quotes.index(median_quote))
    short_quote = [quote for quote in raw_quotes if int(quote["c"]) < median][0]
    long_quote = [quote for quote in raw_quotes if int(quote["c"]) > median][0]

    # extract run date from the triggering asset
    run_date = _get_run_date(triggering_asset=raw_zen_quotes, context=context)

    # attach the run date to the asset
    yield Metadata(Asset("selected_quotes"), {"run_date": run_date})

    return {
        "median_q": median_quote,
        "short_q": short_quote,
        "long_q": long_quote,
    }


@asset(schedule=[selected_quotes])
def formatted_newsletter(context: dict):
    """
    Formats the newsletter.
    """
    object_storage_path = ObjectStoragePath(
        f"{OBJECT_STORAGE_SYSTEM}://{OBJECT_STORAGE_PATH_NEWSLETTER}",
        conn_id=OBJECT_STORAGE_CONN_ID,
    )

    quotes = context["ti"].xcom_pull(
        dag_id="selected_quotes",
        task_ids=["selected_quotes"],
        key="return_value",
        include_prior_dates=True,
    )[0]

    # extract run date from the triggering asset
    run_date = _get_run_date(triggering_asset=selected_quotes, context=context)

    # attach the run date to the asset event
    yield Metadata(Asset("formatted_newsletter"), {"run_date": run_date})

    newsletter_template_path = object_storage_path / "newsletter_template.txt"
    newsletter_template = newsletter_template_path.read_text()

    newsletter = newsletter_template.format(
        quote_text_1=quotes["short_q"]["q"],
        quote_author_1=quotes["short_q"]["a"],
        quote_text_2=quotes["median_q"]["q"],
        quote_author_2=quotes["median_q"]["a"],
        quote_text_3=quotes["long_q"]["q"],
        quote_author_3=quotes["long_q"]["a"],
        date=run_date,
    )

    date_newsletter_path = object_storage_path / f"{run_date}_newsletter.txt"
    date_newsletter_path.write_text(newsletter)

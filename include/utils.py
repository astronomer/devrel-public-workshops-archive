from datetime import datetime

from airflow import Asset
from airflow.models import DagRun


def get_run_date(context: dict, triggering_asset: Asset = None) -> str | None:
    dag_run: DagRun = context["dag_run"]

    if not dag_run:
        return None

    if triggering_asset and dag_run.run_type == "asset_triggered":
        asset_event = context["triggering_asset_events"][triggering_asset][0]
        return asset_event.extra["run_date"]
    elif dag_run.logical_date:
        return dag_run.logical_date.strftime("%Y-%m-%d")
    else:
        return datetime.now().strftime("%Y-%m-%d")

def process_asset_event(events):
    return [{
        "id": 129,
        "name": "Jan",
        "location": "Bern",
        "motivation": "Find the truth.",
        "favorite_sci_fi_character": "Jadzia (Star Trek)",
    }]

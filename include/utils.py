import json
import time
from datetime import datetime

from airflow import Asset
from airflow.models import DagRun
from airflow.sdk import ObjectStoragePath
from geopy import Nominatim, ArcGIS


def get_run_date(context: dict, triggering_asset: Asset = None) -> str | None:
    dag_run: DagRun = context["dag_run"]

    if not dag_run:
        return None

    if (
        triggering_asset and
        dag_run.run_type == "asset_triggered" and
        triggering_asset in context["triggering_asset_events"] and
        len(context["triggering_asset_events"][triggering_asset]) > 0
    ):
        asset_event = context["triggering_asset_events"][triggering_asset][0]
        return asset_event.extra["run_date"]
    elif dag_run.logical_date:
        return dag_run.logical_date.strftime("%Y-%m-%d")
    else:
        return datetime.now().strftime("%Y-%m-%d")


def get_lat_long(location: str, locations_file: ObjectStoragePath):
    """
    Caches geocoding and uses a fallback provider if Nominatim fails
    """
    if not locations_file.exists():
        locations_file.write_text("{}")
        locations_data = {}
    else:
        content = locations_file.read_text()
        locations_data = json.loads(content) if content else {}

    if location in locations_data:
        return tuple(locations_data[location])

    geolocators = [
        (Nominatim(user_agent="MyApp/1.0 (my_email@example.com)"), "Nominatim"),
        (ArcGIS(), "ArcGIS")
    ]

    coordinates = None
    for geolocator, name in geolocators:
        try:
            if name == "Nominatim":
                time.sleep(5)

            print(f"Attempting geocode with {name}...")
            location_object = geolocator.geocode(location)

            if location_object:
                coordinates = (float(location_object.latitude), float(location_object.longitude))
                break

        except Exception as e:
            print(f"Provider {name} failed: {e}")
            continue

    if coordinates:
        locations_data[location] = coordinates
        locations_file.write_text(json.dumps(locations_data))
        return coordinates
    else:
        raise Exception(f"Could not geocode location: {location} with any provider.")


def extract_user_info_from_asset_extra(asset_extra):
    return [{
        "id": 129,
        "name": "Jan",
        "location": "Bern",
        "motivation": "Find the truth.",
        "favorite_sci_fi_character": "Jadzia (Star Trek)",
    }]

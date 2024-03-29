from apiflask import APIBlueprint, abort
from bilal_backend.utils.utils import db_context
from bilal_backend.libs.pt_handler import prayer_times_handler
from bilal_backend.spec.schemas import PrayerTimesSchemas

prayer_times = APIBlueprint(
    import_name="Prayer Times",
    name="Prayer Times",
    tag="Prayer Times",
    url_prefix="/prayer-times",
)


@prayer_times.get("/")
@prayer_times.output(PrayerTimesSchemas)
@prayer_times.doc(responses=[200, 412])
@db_context
def get_prayer_times(data):
    calc = data.get("calculation", {}).get("method", {})
    jur = data.get("calculation", {}).get("jurisprudence", "Standard")
    location = data.get("location", {})
    lat = location.get("lat")
    long = location.get("long")
    tz = location.get("tz")
    if not all([calc, jur, lat, long, tz]):
        abort(
            status_code=412,
            message=f"No user settings found. calc = {calc}, location = {location}",
        )
    return prayer_times_handler(
        lat=location.get("lat"),
        long=location.get("long"),
        tz=location.get("tz"),
        calc=calc,
        jur=jur,
    )

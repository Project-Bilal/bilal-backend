from apiflask import APIBlueprint, output, abort
from lightdb import LightDB

from bilal_backend.libs.constants import DATA_FILE
from bilal_backend.libs.prayer_times_handler import prayer_times_handler
from bilal_backend.spec.schemas import PrayerTimesSchemas

prayer_times = APIBlueprint(import_name="Prayer Times",
                            name="Prayer Times",
                            tag="Prayer Times",
                            url_prefix='/prayer-times')


@prayer_times.get('/')
@output(PrayerTimesSchemas)
def get_prayer_times():
    data = LightDB(DATA_FILE)
    calc = data.get('calculation')
    location = data.get('location')
    if not calc or not location or 'lat' not in location or 'long' not in location or 'tz' not in location:
        abort(status_code=500, message="No user settings found")
    return prayer_times_handler(lat=float(location.get('lat')),
                                long=float(location.get('long')),
                                tz=location.get('tz'),
                                calc=calc)

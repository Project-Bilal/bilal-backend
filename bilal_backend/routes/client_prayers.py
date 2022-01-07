from apiflask import APIBlueprint, output, abort, doc
from bilal_backend.utils.utils import db_context

from bilal_backend.libs.constants import DATA_FILE
from bilal_backend.libs.pt_handler import prayer_times_handler
from bilal_backend.spec.schemas import PrayerTimesSchemas, CalculationsSchema
from bilal_backend.utils.utils import calculations

prayer_times = APIBlueprint(import_name="Prayer Times",
                            name="Prayer Times",
                            tag="Prayer Times",
                            url_prefix='/prayer-times')

@db_context
@prayer_times.get('/')
@output(PrayerTimesSchemas)
@doc(responses=[200, 412])
def get_prayer_times(data):
    data = data(DATA_FILE)
    calc = data.get('calculation')
    location = data.get('location')
    if not calc or not location or 'lat' not in location or 'long' not in location or 'tz' not in location:
        abort(status_code=412, message=f"No user settings found. calc = {calc}, location = {location}")
    return prayer_times_handler(lat=location.get('lat'),
                                long=location.get('long'),
                                tz=location.get('tz'),
                                calc=calc)


@prayer_times.get('/calculations')
@doc(responses=[200])
def get_calculations():
    return calculations

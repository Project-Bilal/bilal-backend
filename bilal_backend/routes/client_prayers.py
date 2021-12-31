from datetime import date

from apiflask import APIBlueprint, output
from lightdb import LightDB

from bilal_backend.libs.prayer_times import PrayTimes
from bilal_backend.spec.schemas import PrayerTimesSchemas

prayer_times = APIBlueprint(import_name="Prayer Times",
                            name="Prayer Times",
                            tag="Prayer Times",
                            url_prefix='/prayer-times')


@prayer_times.get('/')
@output(PrayerTimesSchemas)
def get_prayer_times():
    data = LightDB('bilal_backend/db/data.json')
    pray_times = PrayTimes(calMethod=data.get('calculation'))
    location = data.get('location')
    today = date.today()
    times = pray_times.getTimes(
        date=today,
        coords=(float(location.get('lat')), float(location.get('long'))),
        timezone=-8,
    )
    return times

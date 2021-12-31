from datetime import date

from bilal_backend.libs.prayer_times import PrayTimes
from lightdb import LightDB

from apiflask import APIBlueprint

prayer_times = APIBlueprint(import_name="Prayer Times", name="Prayer Times", tag="Prayer Times",
                            url_prefix='/prayer-times')


@prayer_times.get('/')
async def get_prayer_times():
    data = LightDB('bilal_server/db/data.json')

    pray_times = PrayTimes(data.get('calculation'))
    location = data.get('location')
    today = date.today()
    times = pray_times.getTimes(
        date=today,
        coords=(float(location.get('lat')), float(location.get('long'))),
        timezone=-8,
    )
    return times

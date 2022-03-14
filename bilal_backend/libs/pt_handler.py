import datetime
import pytz
import time

from bilal_backend.libs.constants import JURISPRUDENCE
from bilal_backend.utils.prayer_times import PrayTimes


def prayer_times_handler(
    lat=None, long=None, tz=None, calc=None, format=None, jur=JURISPRUDENCE
):
    dt = time.localtime()
    pray_times = PrayTimes(calMethod=calc)
    pray_times.adjust({"asr": jur})

    date = datetime.datetime.now(pytz.timezone(tz))
    # total seconds offset / minutes / hours to give total hours offset
    tz_offset = date.utcoffset().total_seconds() / 60 / 60

    if dt.tm_isdst == 0:
        tz_offset -= 1

    return pray_times.getTimes(
        date=(dt.tm_year, dt.tm_mon, dt.tm_mday),
        coords=(lat, long),
        timezone=tz_offset,
        format=format,
    )

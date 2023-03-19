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
    
    timezone = pytz.timezone(tz)
    now = datetime.datetime.now(timezone)
    is_dst = now.dst() != datetime.timedelta(0)
    offset = now.utcoffset().total_seconds() / 3600
    if is_dst:
        tz_offset += 1
    
    return pray_times.getTimes(
        date=(dt.tm_year, dt.tm_mon, dt.tm_mday),
        coords=(lat, long),
        timezone=tz_offset,
        format=format,
    )

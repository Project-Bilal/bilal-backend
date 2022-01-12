from bilal_backend.libs.constants import JURISPRUDENCE
from bilal_backend.utils.prayer_times import PrayTimes
import time


def prayer_times_handler(
    lat=None, long=None, tz=None, calc=None, format=None, jur=JURISPRUDENCE
):
    dt = time.localtime()
    pray_times = PrayTimes(calMethod=calc)
    pray_times.adjust({"asr": jur})
    return pray_times.getTimes(
        date=(dt.tm_year, dt.tm_mon, dt.tm_mday),
        coords=(lat, long),
        timezone=tz,
        format=format,
        dst=dt.tm_isdst,
    )

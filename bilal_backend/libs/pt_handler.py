from datetime import date

from bilal_backend.utils.prayer_times import PrayTimes

# TODO add option to prayTimes.adjust({'asr': 'Hanafi'})
# TODO add functionality to account for DST
def prayer_times_handler(
    lat=None, long=None, tz=None, calc=None, format=None, jur=None
):
    pray_times = PrayTimes(calMethod=calc)
    if jur:
        PrayTimes.adjust({"asr": jur})
    return pray_times.getTimes(
        date=date.today(), coords=(lat, long), timezone=tz, format=format
    )

from datetime import date

from bilal_backend.libs.prayer_times import PrayTimes


def prayer_times_handler(lat=None, long=None, tz=None, calc=None):
    pray_times = PrayTimes(calMethod=calc)
    return pray_times.getTimes(date=date.today(), coords=(lat, long), timezone=tz)

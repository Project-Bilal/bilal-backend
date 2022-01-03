from functools import wraps
import pytz
from tzwhere import tzwhere
from datetime import datetime
from bilal_backend.db.LightDB import LightDB
from bilal_backend.libs.constants import DATA_FILE


def get_tz(lat, long):
    # Get timezone string from lat/long
    tz = tzwhere.tzwhere()
    tz_str = tz.tzNameAt(lat, long)
    # Get current date to determine offset
    dt = datetime.now(pytz.timezone(tz_str))
    # total seconds offset / minutes / hours to give total hours offset
    return dt.utcoffset().total_seconds() / 60 / 60


def db_context(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        data = LightDB(DATA_FILE)
        return f(data, *args, **kwargs)

    return wrapper

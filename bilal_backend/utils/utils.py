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


calculations = {
    "MWL": {
        "name": "Muslim World League",
        "key": "MWL",
        "params": {"fajr": 18, "isha": 17},
    },
    "ISNA": {
        "name": "Islamic Society of North America (ISNA)",
        "key": "ISNA",
        "params": {"fajr": 15, "isha": 15},
    },
    "Egypt": {
        "name": "Egyptian General Authority of Survey",
        "key": "Egypt",
        "params": {"fajr": 19.5, "isha": 17.5},
    },
    "Makkah": {
        "name": "Umm Al-Qura University, Makkah",
        "key": "Makkah",
        "params": {
            "fajr": 18.5,
            "isha": "90 min",
        },  # fajr was 19 degrees before 1430 hijri
    },
    "Karachi": {
        "name": "University of Islamic Sciences, Karachi",
        "key": "Karachi",
        "params": {"fajr": 18, "isha": 18},
    },
    "Tehran": {
        "name": "Institute of Geophysics, University of Tehran",
        "key": "Tehran",
        "params": {"fajr": 17.7, "isha": 14, "maghrib": 4.5, "midnight": "Jafari"},
    },
    # isha is not explicitly specified in this method
    "Jafari": {
        "name": "Shia Ithna-Ashari, Leva Institute, Qum",
        "key": "Jafari",
        "params": {"fajr": 16, "isha": 14, "maghrib": 4, "midnight": "Jafari"},
    },
    # Added Calculations
    "Moon": {
        "name": "Moonsighting Committee",
        "key": "Moon",
        "params": {"fajr": 18, "isha": 18},
    },
    "UAE": {
        "name": "Authority of Dubai, UAE",
        "key": "UAE",
        "params": {"fajr": 18.2, "isha": 18.2},
    },
    "Kuwait": {
        "name": "Authority of Kuwait",
        "key": "Kuwait",
        "params": {"fajr": 18, "isha": 17.5},
    },
    "Qatar": {
        "name": "Authority of Qatar",
        "key": "Qatar",
        "params": {"fajr": 18, "isha": "90 min"},
    },
    "Singapore": {
        "name": "Majlis Ugama Islam Singapura",
        "key": "Singapore",
        "params": {"fajr": 20, "isha": 18},
    },
    "Jakarta": {
        "name": "KEMENEG Jakarta Pusat",
        "key": "Jakarta",
        "params": {"fajr": 20, "isha": 18},
    },
    "Turkey": {
        "name": "Diyanet Isleri Baskanligi, Turkey",
        "key": "Turkey",
        "params": {"fajr": 18, "isha": 17},
    },
    "France": {
        "name": "Union of Islamic Orgs. of France",
        "key": "France",
        "params": {"fajr": 12, "isha": 12},
    },
    "Russia": {
        "name": "Spiritual Administration of Muslims of Russia",
        "key": "Russia",
        "params": {"fajr": 16, "isha": 15},
    },
    "Tunisia": {
        "name": "Tunisian Ministry of Religious Affairs",
        "key": "Tunisia",
        "params": {"fajr": 10, "isha": 10},
    },
    "Algeria": {
        "name": "Algerian Ministry of Religious Affairs and Wakfs",
        "key": "Algeria",
        "params": {"fajr": 18, "isha": 17},
    },
}

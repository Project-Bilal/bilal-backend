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
        db = LightDB(DATA_FILE)
        resp = f(db, *args, **kwargs)
        db.save()
        return resp

    return wrapper


def athans_settings_context(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        data = args[0]
        prayer = args[1]
        athans = data.get('athans', {})
        prayer_athan_settings = athans.get(prayer, {})

        prayer_athan_settings = f(prayer_athan_settings, *args, **kwargs)

        athans.update({prayer: prayer_athan_settings})
        data.set('athans', athans)

    return wrapper


jurisprudence = [{'label': 'Standard', 'details': "Shafa'i, Malaki, Hambali"},
                 {'label': 'Hanafi', 'details': "Hanafi"}]

calculations = {
    "MWL": {
        "name": "Muslim World League",
        "method": "MWL",
        "params": {"fajr": 18, "isha": 17},
    },
    "ISNA": {
        "name": "Islamic Society of North America (ISNA)",
        "method": "ISNA",
        "params": {"fajr": 15, "isha": 15},
    },
    "Egypt": {
        "name": "Egyptian General Authority of Survey",
        "method": "Egypt",
        "params": {"fajr": 19.5, "isha": 17.5},
    },
    "Makkah": {
        "name": "Umm Al-Qura University, Makkah",
        "method": "Makkah",
        "params": {
            "fajr": 18.5,
            "isha": "90 min",
        },  # fajr was 19 degrees before 1430 hijri
    },
    "Karachi": {
        "name": "University of Islamic Sciences, Karachi",
        "method": "Karachi",
        "params": {"fajr": 18, "isha": 18},
    },
    "Tehran": {
        "name": "Institute of Geophysics, University of Tehran",
        "method": "Tehran",
        "params": {"fajr": 17.7, "isha": 14, "maghrib": 4.5, "midnight": "Jafari"},
    },
    # isha is not explicitly specified in this method
    "Jafari": {
        "name": "Shia Ithna-Ashari, Leva Institute, Qum",
        "method": "Jafari",
        "params": {"fajr": 16, "isha": 14, "maghrib": 4, "midnight": "Jafari"},
    },
    # Added Calculations
    "Moon": {
        "name": "Moonsighting Committee",
        "method": "Moon",
        "params": {"fajr": 18, "isha": 18},
    },
    "UAE": {
        "name": "Authority of Dubai, UAE",
        "method": "UAE",
        "params": {"fajr": 18.2, "isha": 18.2},
    },
    "Kuwait": {
        "name": "Authority of Kuwait",
        "method": "Kuwait",
        "params": {"fajr": 18, "isha": 17.5},
    },
    "Qatar": {
        "name": "Authority of Qatar",
        "method": "Qatar",
        "params": {"fajr": 18, "isha": "90 min"},
    },
    "Singapore": {
        "name": "Majlis Ugama Islam Singapura",
        "method": "Singapore",
        "params": {"fajr": 20, "isha": 18},
    },
    "Jakarta": {
        "name": "KEMENEG Jakarta Pusat",
        "method": "Jakarta",
        "params": {"fajr": 20, "isha": 18},
    },
    "Turmethod": {
        "name": "Diyanet Isleri Baskanligi, Turmethod",
        "method": "Turmethod",
        "params": {"fajr": 18, "isha": 17},
    },
    "France": {
        "name": "Union of Islamic Orgs. of France",
        "method": "France",
        "params": {"fajr": 12, "isha": 12},
    },
    "Russia": {
        "name": "Spiritual Administration of Muslims of Russia",
        "method": "Russia",
        "params": {"fajr": 16, "isha": 15},
    },
    "Tunisia": {
        "name": "Tunisian Ministry of Religious Affairs",
        "method": "Tunisia",
        "params": {"fajr": 10, "isha": 10},
    },
    "Algeria": {
        "name": "Algerian Ministry of Religious Affairs and Wakfs",
        "method": "Algeria",
        "params": {"fajr": 18, "isha": 17},
    },
}

from lightdb import LightDB
from bilal_backend.libs.constants import DATA_FILE
from bilal_backend.libs.utils import get_tz

'''
{
    'location': {'long': int,
                 'lat': int,
                 },
    'calculation': str,
    'athan_default': str,
    'athan_fajir': str,
    'athan_delay': int,
    'speaker_name': str,
    'speaker_volume': float,

}
'''

ATHANS = {
    'id': {
        'name': str,
        'id': str,
        'length': str,
    }
}
FAJIR_ATHANS = {
    'id': {
        'name': str,
        'id': str,
        'length': str,
    }
}


def get_user_location():
    data = LightDB(DATA_FILE)
    return data.get('location')


def set_user_location(lat, long, address):
    data = LightDB(DATA_FILE)
    tz = get_tz(lat, long)
    location = {
        'address': address,
        'lat': lat,
        'long': long,
        'tz': tz
    }
    data.set('location', location)
    # TODO run cron jobs script


def get_user_calculation():
    data = LightDB(DATA_FILE)
    return data.get('calculation')


def set_user_calculation(calculation):
    data = LightDB(DATA_FILE)
    data.set('calculation', calculation)
    # TODO run cron jobs script


def get_user_athan():
    data = LightDB(DATA_FILE)
    # TODO: Create dictionary for athans, and return athan details
    return data.get('athan_default')


def set_user_athan(athan):
    data = LightDB(DATA_FILE)
    data.set('athan_default', athan)


def get_user_fajir_athan():
    data = LightDB(DATA_FILE)
    return data.get('athan_fajir')


def set_user_fajir_athan(athan):
    data = LightDB(DATA_FILE)
    data.set('athan_fajir', athan)


def get_user_athan_delay():
    data = LightDB(DATA_FILE)
    return data.get('athan_delay')


def set_user_athan_delay(delay):
    data = LightDB(DATA_FILE)
    data.set('athan_delay', delay)


def get_speaker_name():
    data = LightDB(DATA_FILE)
    return data.get('speaker_name')


def set_speaker_name(name):
    data = LightDB(DATA_FILE)
    data.set('speaker_name', name)


def get_speaker_volume():
    data = LightDB(DATA_FILE)
    return data.get('speaker_volume')


def set_speaker_volume(volume):
    data = LightDB(DATA_FILE)
    data.set('speaker_volume', volume)


def reset():
    data = LightDB(DATA_FILE)
    data.reset()

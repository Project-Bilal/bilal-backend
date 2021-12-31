from lightdb import LightDB

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
    data = LightDB('bilal_server/db/data.json')
    return data.get('location')


def set_user_location(location):
    data = LightDB('bilal_server/db/data.json')
    data.set('location', location)


def get_user_calculation():
    data = LightDB('bilal_server/db/data.json')
    return data.get('calculation')


def set_user_calculation(calculation):
    data = LightDB('bilal_server/db/data.json')
    data.set('calculation', calculation)


def get_user_athan():
    data = LightDB('bilal_server/db/data.json')
    # TODO: Create dictionary for athans, and return athan details
    return data.get('athan_default')


def set_user_athan(athan):
    data = LightDB('bilal_server/db/data.json')
    data.set('athan_default', athan)


def get_user_fajir_athan():
    data = LightDB('bilal_server/db/data.json')
    return data.get('athan_fajir')


def set_user_fajir_athan(athan):
    data = LightDB('bilal_server/db/data.json')
    data.set('athan_fajir', athan)


def get_user_athan_delay():
    data = LightDB('bilal_server/db/data.json')
    return data.get('athan_delay')


def set_user_athan_delay(delay):
    data = LightDB('bilal_server/db/data.json')
    data.set('athan_delay', delay)


def get_speaker_name():
    data = LightDB('bilal_server/db/data.json')
    return data.get('speaker_name')


def set_speaker_name(name):
    data = LightDB('bilal_server/db/data.json')
    data.set('speaker_name', name)


def get_speaker_volume():
    data = LightDB('bilal_server/db/data.json')
    return data.get('speaker_volume')


def set_speaker_volume(volume):
    data = LightDB('bilal_server/db/data.json')
    data.set('speaker_volume', volume)


def reset():
    data = LightDB('bilal_server/db/data.json')
    data.reset()

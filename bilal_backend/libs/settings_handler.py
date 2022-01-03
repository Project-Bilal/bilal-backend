from bilal_backend.libs.utils import get_tz, db_context

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


@db_context
def get_user_location(data):
    return data.get('location')


@db_context
def set_user_location(data, lat, long, address):
    tz = get_tz(lat, long)
    location = {
        'address': address,
        'lat': lat,
        'long': long,
        'tz': tz
    }
    data.set('location', location)

    # TODO run cron jobs script


@db_context
def get_user_calculation(data):
    return data.get('calculation')


@db_context
def set_user_calculation(data, calculation):
    data.set('calculation', calculation)
    # TODO run cron jobs script


@db_context
def get_user_athan(data):
    # TODO: Create dictionary for athans, and return athan details
    return data.get('athan_default')


@db_context
def set_user_athan(data, athan):
    data.set('athan_default', athan)


@db_context
def get_user_fajir_athan(data):
    return data.get('athan_fajir')


@db_context
def set_user_fajir_athan(data, athan):
    data.set('athan_fajir', athan)


@db_context
def get_user_athan_delay(data):
    return data.get('athan_delay')


@db_context
def set_user_athan_delay(data, delay):
    data.set('athan_delay', delay)


@db_context
def get_speaker(data):
    return data.get('speaker')


@db_context
def set_speaker(data, speaker):
    data.set('speaker', speaker)


@db_context
def get_speaker_volume(data):
    return data.get('speaker_volume')


@db_context
def set_speaker_volume(data, volume):
    data.set('speaker_volume', volume)


@db_context
def reset(data):
    data.reset()

from bilal_backend.utils.utils import get_tz, db_context


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
def get_volume(data):
    return data.get('speaker_volume')


@db_context
def set_volume(data, volume):
    data.set('speaker_volume', volume)


@db_context
def reset(data):
    data.reset()

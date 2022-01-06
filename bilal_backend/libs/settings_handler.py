from bilal_backend.utils.utils import get_tz, db_context
from bilal_backend.scripts.schedule_notifications import sched_notifications


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
    sched_notifications()


@db_context
def get_user_calculation(data):
    calc = data.get('calculation')
    return calculations.get(calc)


@db_context
def set_user_calculation(data, calculation):
    data.set('calculation', calculation)
    sched_notifications()


@db_context
def get_speaker(data):
    return data.get('speaker')


@db_context
def set_speaker(data, speaker: dict):
    data.set('speaker', speaker)


@db_context
def get_volume(data):
    d = data.get('speaker')
    return d.get('volume')


@db_context
def set_volume(data, volume: dict):
    speaker = data.get('speaker')
    speaker.update(volume)
    data.set('speaker', speaker)


@db_context
def reset(data):
    data.reset()

from bilal_backend.utils.utils import get_tz, db_context, calculations
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
    calc = data.get('calculation', {})
    method = calc.get('method')
    calc.update({'method': calculations.get(method, {})})
    return calc


@db_context
def set_method(data, method):
    calc = data.get('calculation', {})
    calc.update({'method': method})
    data.set('calculation', calc)
    sched_notifications()


@db_context
def set_jurisprudence(data, jurisprudence):
    calc = data.get('calculation', {})
    calc.update({'jurisprudence': jurisprudence})
    data.set('calculation', calc)
    sched_notifications()


@db_context
def get_speaker(data):
    return data.get('speaker')


@db_context
def set_speaker(data, speaker: dict):
    data.set('speaker', speaker)


@db_context
def reset(data):
    data.reset()

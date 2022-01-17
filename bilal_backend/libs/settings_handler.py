from datetime import datetime
import pytz
from pytz.exceptions import UnknownTimeZoneError
from bilal_backend.utils.audio_ids import audio
from bilal_backend.utils.utils import db_context, calculations, jurisprudence


@db_context
def get_user_location(data):
    return data.get("location")


@db_context
def set_user_location(data, lat, long, timezone):
    try:  # check timezone is legit
        datetime.now(pytz.timezone(timezone))
    except UnknownTimeZoneError:
        return False
    location = {
        'lat': lat,
        'long': long,
        'tz': timezone
    }
    data.set('location', location)
    return True


@db_context
def get_user_calculation(data):
    calc = data.get("calculation", {})
    method = calc.get("method")
    calc.update({"method": calculations.get(method, {})})
    return calc


@db_context
def set_method(data, method):
    calc = data.get("calculation", {})
    calc.update({"method": method})
    data.set("calculation", calc)
    return True


@db_context
def set_jurisprudence(data, jurisprudence):
    calc = data.get("calculation", {})
    calc.update({"jurisprudence": jurisprudence})
    data.set("calculation", calc)
    return True


@db_context
def get_speaker(data):
    return data.get("speaker")


@db_context
def set_speaker(data, speaker: dict):
    data.set("speaker", speaker)


@db_context
def reset(data):
    data.reset()


@db_context
def get_all(data):
    resp = {}
    resp.update({'methods': calculations})
    resp.update({'jurisprudence': jurisprudence})
    resp.update({'audio': audio})
    if data:
        resp.update(data)
    return resp

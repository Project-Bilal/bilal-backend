from bilal_backend.utils.utils import db_context
from bilal_backend.utils.audio_ids import audio
from bilal_backend.scripts.schedule_notifications import sched_notifications


@db_context
def get_fajir_athan(data):
    audio_id = data.get('fajir_athan')
    if not audio_id:
        return None
    return audio.get(audio_id['audio_id'])


@db_context
def set_fajir_athan(data, id):
    data.set('fajir_athan', id)


@db_context
def get_dhuhr_athan(data):
    audio_id = data.get('dhuhr_athan')
    if not audio_id:
        return None
    return audio.get(audio_id['audio_id'])


@db_context
def set_dhuhr_athan(data, id):
    data.set('dhuhr_athan', id)


@db_context
def get_asr_athan(data):
    audio_id = data.get('asr_athan')
    if not audio_id:
        return None
    return audio.get(audio_id['audio_id'])


@db_context
def set_asr_athan(data, id):
    data.set('asr_athan', id)


@db_context
def get_mughrib_athan(data):
    audio_id = data.get('mughrib_athan')
    if not audio_id:
        return None
    return audio.get(audio_id['audio_id'])


@db_context
def set_mughrib_athan(data, id):
    data.set('mughrib_athan', id)


@db_context
def get_isha_athan(data):
    audio_id = data.get('isha_athan')
    if not audio_id:
        return None
    return audio.get(audio_id['audio_id'])


@db_context
def set_isha_athan(data, id):
    data.set('isha_athan', id)


@db_context
def get_notification(data):
    audio_id = data.get('notification_id')
    if not audio_id:
        return None
    return audio.get(audio_id['audio_id'])


@db_context
def set_notification(data, id):
    data.set('notification_id', id)

def schedule_notifications():
    if not sched_notifications():
        return None
    return "Notifications scheduled"

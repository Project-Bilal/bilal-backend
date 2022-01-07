from bilal_backend.utils.utils import db_context
from bilal_backend.utils.audio_ids import audio
from bilal_backend.scripts.schedule_notifications import sched_notifications


@db_context
def get_athan(data, prayer):
    audio_id = data.get(prayer)
    return audio.get(audio_id.get('audio_id'))


@db_context
def set_athan(data, prayer, audio_id):
    data.set(prayer, audio_id)


def schedule_notifications():
    if not sched_notifications():
        return None
    return "Notifications scheduled"

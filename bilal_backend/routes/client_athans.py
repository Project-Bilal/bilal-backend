from apiflask import APIBlueprint, abort
from bilal_backend.utils.audio_ids import audio
from bilal_backend.libs import athans_handler as handler
from bilal_backend.libs.constants import SUCCESS
from bilal_backend.scripts.schedule_notifications import sched_notifications

athans = APIBlueprint(import_name="Athans", name="Athans", tag="Athan", url_prefix='/athans')


@athans.get('/')
def get_athans():
    return audio


@athans.get('/settings')
def get_athans_settings():
    resp = handler.get_athan_settings()
    if not resp:
        abort(status_code=412, message="no athans settings saved")
    return resp


@athans.put('/<string:prayer>/volume/<int:volume>')
def set_athan_volume(prayer: str, volume: int):
    handler.set_volume(prayer, volume)
    return SUCCESS


@athans.put('/<string:prayer>/athan/<string:audio_id>')
def set_athan_audio(prayer, audio_id):
    handler.set_athan(prayer, audio_id)
    return SUCCESS


@athans.put('/<string:prayer>/notification/<string:audio_id>')
def set_notification_audio(prayer, audio_id):
    handler.set_notification(prayer, audio_id)
    return SUCCESS


@athans.put('/<string:prayer>/notification-time/<int:notification_time>')
def set_notification_time(prayer, notification_time):
    handler.set_notif_time(prayer, notification_time)
    return SUCCESS


@athans.get('/schedule')
def schedule_notifications():
    if not sched_notifications():
        abort(status_code=412, message="Did not schedule the notifications")
    return "Notifications scheduled"

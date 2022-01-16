from apiflask import APIBlueprint, abort, input
from bilal_backend.utils.audio_ids import audio
from bilal_backend.libs import athans_handler as handler
from bilal_backend.libs.constants import SUCCESS
from bilal_backend.scripts.schedule_notifications import sched_notifications
from bilal_backend.spec.schemas import Toggle

athans = APIBlueprint(import_name="Athans", name="Athans", tag="Athan", url_prefix='/athans')


@athans.get('/')
def get_athans():
    return audio


@athans.get('/settings')
def get_athans_settings():
    return handler.get_athan_settings()


@athans.put('/<string:prayer>/volume/<int:volume>')
def set_athan_volume(prayer: str, volume: int):
    handler.set_volume(prayer, volume)
    print(sched_notifications())
    return SUCCESS


@athans.put('/<string:prayer>/athan/<string:audio_id>')
def set_athan_audio(prayer, audio_id):
    handler.set_athan(prayer, audio_id)
    print(sched_notifications())
    return SUCCESS


@athans.put('/<string:prayer>/notification/<string:audio_id>')
def set_notification_audio(prayer, audio_id):
    handler.set_notification(prayer, audio_id)
    print(sched_notifications())
    return SUCCESS


@athans.put('/<string:prayer>/notification-time/<int:notification_time>')
def set_notification_time(prayer, notification_time):
    handler.set_notif_time(prayer, notification_time)
    print(sched_notifications())
    return SUCCESS


@athans.put('/<string:prayer>/toggle-athan')
@input(Toggle, location='query')
def toggle_athan(prayer, on):
    athan_on = on.get('on')
    handler.toggle_athan(prayer, athan_on)
    print(sched_notifications())
    return SUCCESS


@athans.put('/<string:prayer>/toggle-notification')
@input(Toggle, location='query')
def toggle_notification(prayer, on):
    notification_on = on.get('on')
    handler.toggle_notification(prayer, notification_on)
    print(sched_notifications())
    return SUCCESS


@athans.get('/schedule')
def schedule_notifications():
    if 'ERROR' in sched_notifications():
        abort(status_code=412, message="Did not schedule the notifications")
    return "Notifications scheduled"

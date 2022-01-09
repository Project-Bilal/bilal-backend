from bilal_backend.utils.utils import db_context, athans_settings_context
from bilal_backend.utils.audio_ids import audio


@db_context
@athans_settings_context
def set_athan(prayer_athan_settings, data, prayer, audio_id):
    prayer_athan_settings.update({'audio_id': audio_id})
    return prayer_athan_settings


@db_context
@athans_settings_context
def set_volume(prayer_athan_settings, data, prayer, volume):
    prayer_athan_settings.update({'volume': volume})
    return prayer_athan_settings


@db_context
@athans_settings_context
def set_notification(prayer_athan_settings, data, prayer, notification_audio):
    prayer_athan_settings.update({'notification_id': notification_audio})
    return prayer_athan_settings


@db_context
@athans_settings_context
def set_notif_time(prayer_athan_settings, data, prayer, notification_time):
    prayer_athan_settings.update({'notification_time': notification_time})
    return prayer_athan_settings


@db_context
@athans_settings_context
def toggle_athan(prayer_athan_settings, data, prayer, athan_on):
    prayer_athan_settings.update({'athan_on': athan_on})
    return prayer_athan_settings


@db_context
@athans_settings_context
def toggle_notification(prayer_athan_settings, data, prayer, notification_on):
    prayer_athan_settings.update({'notification_on': notification_on})
    return prayer_athan_settings


@db_context
def get_athan_settings(data):
    return data.get('athans')

from bilal_backend.utils.utils import db_context


@db_context
def get_fajir_athan(data):
    return data.get('fajir_athan')


@db_context
def set_fajir_athan(data, id):
    data.set('fajir_athan', id)


@db_context
def get_dhuhr_athan(data):
    return data.get('dhuhr_athan')


@db_context
def set_dhuhr_athan(data, id):
    data.set('dhuhr_athan', id)


@db_context
def get_asr_athan(data):
    return data.get('asr_athan')


@db_context
def set_asr_athan(data, id):
    data.set('asr_athan', id)


@db_context
def get_mughrib_athan(data):
    return data.get('mughrib_athan')


@db_context
def set_mughrib_athan(data, id):
    data.set('mughrib_athan', id)


@db_context
def get_isha_athan(data):
    return data.get('isha_athan')


@db_context
def set_isha_athan(data, id):
    data.set('isha_athan', id)


@db_context
def get_notification(data):
    return data.get('notification_id')


@db_context
def set_notification(data, id):
    data.set('notification_id', id)

from bilal_backend.utils.utils import db_context



@db_context
def get_athan_settings(data):
    return data.get('athans', {})

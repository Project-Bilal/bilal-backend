from bilal_backend.utils.utils import db_context


@db_context
def reset(data):
    data.reset()


@db_context
def get_all(data):
    return data


@db_context
def set_all(data, user_settings):
    data.set('settings', user_settings)
    return True

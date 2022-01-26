
from bilal_backend.utils.utils import db_context


@db_context
def reset(data):
    data.reset()


@db_context
def get_all(data):
    return data

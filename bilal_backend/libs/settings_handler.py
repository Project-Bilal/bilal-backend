from bilal_backend.utils.utils import db_context
from subprocess import run


@db_context
def reset(data):
    data.reset()


@db_context
def get_all(data):
    return data


@db_context
def set_all(data, user_settings):
    data.set("settings", user_settings)
    tz = data.get("settings", {}).get("tz", {})
    if not tz:
        return False
    rc = run(f"sudo timedatectl set-timezone {tz}", shell=True).returncode
    if rc != 0:
        return False
    return True

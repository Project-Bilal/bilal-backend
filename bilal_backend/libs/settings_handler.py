from bilal_backend.utils.utils import db_context
from bilal_backend.libs.chromecast_handler import get_speaker
from subprocess import run


@db_context
def reset(data):
    data.reset()


@db_context
def get_all(data):
    return data


@db_context
def set_all(data, user_settings):
    tz = user_settings.get("tz", {})
    speaker_name = user_settings.get("speaker", {})
    if not tz or not speaker_name:
        return False
    rc = run(f"sudo timedatectl set-timezone {tz}", shell=True).returncode
    speaker_info = get_speaker(speaker_name)
    if rc != 0 or not speaker_info:
        return False
    user_settings["speaker"] = speaker_info
    data.set("settings", user_settings)
    return True


def update():
    rc = run(f"git pull origin master", shell=True).returncode
    if rc != 0:
        return False
    rc = run(f"sudo systemctl restart bilal.service", shell=True).returncode
    if rc != 0:
        return False
    return True

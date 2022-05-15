from pychromecast import (
    threading,
    CastBrowser,
    SimpleCastListener,
    get_chromecast_from_host,
    get_listed_chromecasts,
    discovery,
)
from zeroconf import Zeroconf
from uuid import UUID
from bilal_backend.libs.constants import (
    DISCOVER_TIMEOUT,
    GOOGLE_STORAGE_URL,
    THUMB,
    DEFAULT_AUDIO_TITLE,
)
from bilal_backend.utils.utils import db_context


# Uses the discover function to return a list of dictionaries for the available speakers
def get_speakers():
    devices, _ = discovery.discover_chromecasts()
    speakers = []
    for device in devices:
        speakers.append(
            {
                "name": device.friendly_name,
                "ip": device.host,
                "port": device.port,
                "uuid": str(device.uuid),
                "model": device.model_name,
                "cast_type": device.cast_type if device.cast_type else "audio",
            }
        )
    return {"speakers": speakers}


def get_speaker(name):
    device = get_listed_chromecasts(friendly_names=[name])[0]
    # check to see if any chromecast was found
    if not device[0]:
        return False
    device = device[0].cast_info
    speaker_info = {
        "cast_type": device.cast_type,
        "port": device.port,
        "name": name,
        "ip": device.host,
        "uuid": str(device.uuid),
        "model": device.model_name,
    }
    return speaker_info


# play on the default speaker given a notification object
def play_notification(audio_id=None, vol=None):
    if not audio_id or not vol:
        return None
    vol /= 100
    device = get_chromecast()
    if not device:
        return {"message": "###ERROR### missing speaker information in 'data.json'"}
    device.wait()
    device.set_volume(vol)
    mc = device.media_controller
    mc.play_media(
        GOOGLE_STORAGE_URL + audio_id,
        "audio/mp3",
        title=DEFAULT_AUDIO_TITLE,
        thumb=THUMB,
    )
    device.disconnect()
    del device
    return {"message": "Sound is played."}


# test a sound on a speaker, dosen't set volume
def test_sound(data):
    device = get_chromecast(data["speaker"])
    device.wait()
    mc = device.media_controller
    mc.play_media(
        GOOGLE_STORAGE_URL + data["audio_id"],
        "audio/mp3",
        title="This is a test from Project-Bilal..",
        thumb=THUMB,
    )
    device.disconnect()
    del device
    return {"message": "Sound is played."}


# return Chromecast object based on host info in db or passed SpeakerSchema
@db_context
def get_chromecast(data, speaker=None):
    spkr = data.get("settings", {}).get("speaker", {}) if not speaker else speaker
    if not spkr:
        print(
            "###ERROR### 'settings' and/or 'speaker' data objects empty or missing in data.json"
        )
        return None
    ip = spkr.get("ip", {})
    port = spkr.get("port", {})
    uuid = UUID(spkr.get("uuid", {}))
    model = spkr.get("model", {})
    name = spkr.get("name", {})
    if not ip or not port or not uuid or not model or not name:
        print("###ERROR### missing speaker information in data.json")
        return None
    host = (ip, port, uuid, model, name)
    return get_chromecast_from_host(host)


# this is a test

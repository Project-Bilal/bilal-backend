from pychromecast import zeroconf, threading, CastBrowser, SimpleCastListener, get_chromecast_from_host
from zeroconf import Zeroconf
from uuid import UUID
from bilal_backend.libs.constants import DISCOVER_TIMEOUT, GDRIVE_URL, TRIES
from bilal_backend.libs.utils import db_context


# Uses the discover function to return a list of dictionaries for the available speakers
def get_speakers():
    devices = discover_devices()
    speakers = []
    for device in devices:
        speakers.append({
            "name": device.friendly_name,
            "ip": device.host,
            "port": device.port,
            "uuid": str(device.uuid),
            "model": device.model_name,
            "cast_type": "Group" if device.cast_type else "Audio",
        })
    return {"speakers": speakers}


# play on the default speaker given an audio_id
@db_context
def play_sound(data, audio_id):
    vol = float(data.get("speaker")['volume']) / 10
    device = get_chromecast()
    device.wait()
    device.set_volume(vol)
    mc = device.media_controller
    mc.play_media(GDRIVE_URL + audio_id, 'audio/mp3')
    return {"message": "Sound is played."}


# test a sound on a speaker, dosen't set volume
def test_sound(data):
    device = get_chromecast(data['speaker'])
    device.wait()
    mc = device.media_controller
    mc.play_media(GDRIVE_URL + data['audio_id'], 'audio/mp3')
    return {"message": "Sound is played."}


# return Chromecast object based on host info in db or passed SpeakerSchema
@db_context
def get_chromecast(data, speaker=None):
    spkr = data.get('speaker') if not speaker else speaker
    host = (
        spkr['ip'],
        spkr['port'],
        UUID(spkr['uuid']),
        spkr['model'],
        spkr['name'],
    )
    return get_chromecast_from_host(host, tries=TRIES)


# discovers all the devices on the network
def discover_devices(max_devices=None, timeout=DISCOVER_TIMEOUT):
    def add_callback(_uuid, _service):
        """Called when zeroconf has discovered a new chromecast."""
        if max_devices is not None and browser.count >= max_devices:
            discover_complete.set()

    discover_complete = threading.Event()
    zconf = Zeroconf()
    browser = CastBrowser(SimpleCastListener(add_callback), zconf)
    browser.start_discovery()

    # Wait for the timeout or the maximum number of devices
    discover_complete.wait(timeout)

    return list(browser.devices.values())

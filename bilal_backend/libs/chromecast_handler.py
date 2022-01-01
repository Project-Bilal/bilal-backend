from pychromecast import threading, zeroconf, CastBrowser, SimpleCastListener, Chromecast
from bilal_backend.libs.constants import DISCOVER_TIMEOUT

# Uses the discover function to return a list of dictionaries for the available speakers
def get_speakers():
    devices = discover_devices()
    speakers = []
    for device in devices:
        speakers.append({
            "name" : device.friendly_name,
            "model" : device.model_name,
            "cast_type" : "Group" if device.cast_type else "Audio",
            "cast_info" : device,
        })
    speakers = {"speakers" : speakers}
    return speakers

# gets a speaker by name, must find all speakers first
def get_speaker(name):
    speakers = get_speakers()
    device = next(speaker for speaker in speakers['speakers'] if speaker["name"] == name)
    return device

#  gets the volume for a speaker by name
def get_volume(name):
    cast_info = get_speaker(name)['cast_info']
    device = get_chromecast(cast_info)
    device.wait()
    vol_level = device.status.volume_level
    return int(round(vol_level, 1) * 10)

# discovers all the devices on the network
def discover_devices(max_devices=None, timeout=DISCOVER_TIMEOUT, zeroconf_instance=None, known_hosts=None):
    def add_callback(_uuid, _service):
        """Called when zeroconf has discovered a new chromecast."""
        if max_devices is not None and browser.count >= max_devices:
            discover_complete.set()

    discover_complete = threading.Event()
    zconf = zeroconf_instance or zeroconf.Zeroconf()
    browser = CastBrowser(SimpleCastListener(add_callback), zconf, known_hosts)
    browser.start_discovery()

    # Wait for the timeout or the maximum number of devices
    discover_complete.wait(timeout)

    return list(browser.devices.values())

# gets a particualr device using the cast_info
def get_chromecast(
    cast_info, tries=None, retry_wait=None, timeout=None
):
    """Creates a Chromecast object from a zeroconf service."""
    return Chromecast(
        cast_info=cast_info,
        tries=tries,
        timeout=timeout,
        retry_wait=retry_wait,
        zconf=zeroconf.Zeroconf(),
    )
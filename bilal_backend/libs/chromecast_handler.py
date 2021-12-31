import pychromecast
from bilal_backend.libs.constants import DATA_FILE

def get_speakers():
    services, browser = pychromecast.discovery.discover_chromecasts()
    pychromecast.discovery.stop_discovery(browser)
    speakers = []
    for device in services:
        speakers.append({
            "name" : device[3],
            "model" : device[2]
        })
    speakers = {"speakers" : speakers}
    return speakers

'''
def get_volume():
    data = db(DATA_FILE)
    speaker = data['speaker_name']
    device = pychromecast.get_listed_chromecasts(friendly_names=[speaker])[0][0]
    # TODO find method that gets volume level
    return "TBA"
'''
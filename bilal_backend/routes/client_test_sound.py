from apiflask import APIBlueprint, input, output
from bilal_backend.libs.constants import GDRIVE_URL
import pychromecast
from bilal_backend.spec.schemas import SoundPlayed, PlaySound

test = APIBlueprint(import_name="Test Sound", name="Test Sound", tag="Test Sound",
                    url_prefix='/test')

@test.post('/')
@input(PlaySound)
@output(SoundPlayed)
def test_sound(data):
    speaker_name = data['speaker_name']
    audio_id = data['audio_id']
    chromecasts = pychromecast.get_listed_chromecasts(friendly_names=[speaker_name])[0]
    cast = chromecasts[0]
    cast.wait()
    mc = cast.media_controller
    mc.play_media(GDRIVE_URL + audio_id, 'audio/mp3')
    return "Sound is played"

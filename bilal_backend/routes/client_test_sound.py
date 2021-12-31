from apiflask import APIBlueprint, Schema, input, output, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
import pychromecast

test = APIBlueprint(import_name="Test Sound", name="Test Sound", tag="Test Sound",
                    url_prefix='/test')


class PlaySound(Schema):
    audio_id = String(required=True)
    speaker_name = String(required=True)


class SoundPlayed(Schema):
    message = String()


@test.post('/')
@input(PlaySound)
@output(SoundPlayed)
def test_sound(data):
    speaker_name = data['speaker_name']
    audio_id = data['audio_id']
    chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[speaker_name])
    cast = chromecasts[0]
    cast.wait()
    cast.set_volume(.5)
    mc = cast.media_controller
    mc.play_media(f'https://drive.google.com/uc?export=download&id={audio_id}', 'audio/mp3')
    return "Sound is played"

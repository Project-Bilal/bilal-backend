from bilal_backend import app
from flask import request
from apiflask import Schema, input, output, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
import pychromecast

class PlaySound(Schema):
    audio_id = String(required=True)
    speaker_name = String(required=True)

class SoundPlayed(Schema):
    message = String()

@app.route('/')
def hello_world():
    return "Hello World"


@app.post('/test-sound')
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
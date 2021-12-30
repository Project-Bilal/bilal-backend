from bilal_backend import app
import pychromecast

@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/test-sound')
def test_sound(speaker_name = 'Studio Display', audio_id = '1jishJEjKVBqMqLhR4uPv8X8hjOKIIvgS'):
    data = request.get_json()
    speaker_name = data['speaker_name']
    audio_id = data['audio_id']
    chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[speaker_name])
    cast = chromecasts[0]
    cast.wait()
    cast.set_volume(.5)
    mc = cast.media_controller
    mc.play_media(f'https://drive.google.com/uc?export=download&id={audio_id}', 'audio/mp3')
    return "Sound is played"
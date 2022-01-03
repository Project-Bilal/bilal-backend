from apiflask import APIBlueprint, output, input, abort, doc
from flask.views import MethodView
from bilal_backend.libs.chromecast_handler import get_speakers, play_sound, test_sound
from bilal_backend.scrap import get_chromecast
from bilal_backend.spec.schemas import SpeakersSchema, PlayedSchema, PlaySchema, TestSoundSchema, SpeakerSchema

speakers = APIBlueprint(import_name="Speaker",
                        name="Speakers",
                        tag="Speakers",
                        url_prefix='/speakers')

@speakers.route('/')
class Speakers(MethodView):
    @output(SpeakersSchema)
    def get(self):
        return get_speakers()



@speakers.route('/play')
class PlaySound(MethodView):
    @input(PlaySchema)
    @output(PlayedSchema)
    def post(self, data):
        return play_sound(data['audio_id'])


@speakers.route('/test')
class TestSound(MethodView):
    @input(TestSoundSchema)
    @output(PlayedSchema)
    def post(self, data):
        return test_sound(data)

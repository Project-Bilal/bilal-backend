from apiflask import APIBlueprint, output, input
from flask.views import MethodView
from bilal_backend.libs.chromecast_handler import get_speakers, play_sound
from bilal_backend.spec.schemas import SpeakersSchema, PlayedSchema, PlaySchema

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
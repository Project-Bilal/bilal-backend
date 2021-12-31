from apiflask import APIBlueprint, output
from flask.views import MethodView
from bilal_backend.libs.chromecast_handler import get_speakers
from bilal_backend.spec.schemas import SpeakersSchema

speakers = APIBlueprint(import_name="Speaker",
                        name="Speakers",
                        tag="Speakers",
                        url_prefix='/speakers')


@speakers.route('/')
class Speakers(MethodView):
    @output(SpeakersSchema)
    def get(self):
        return get_speakers()

'''
@speakers.route('/volume')
class Speakers(MethodView):
    def get(self):
        return get_volume()
'''
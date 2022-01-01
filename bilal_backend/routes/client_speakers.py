from apiflask import APIBlueprint, output
from flask.views import MethodView
from bilal_backend.libs.chromecast_handler import get_speakers, get_volume
from bilal_backend.spec.schemas import SpeakersSchema, VolumeSchema

speakers = APIBlueprint(import_name="Speaker",
                        name="Speakers",
                        tag="Speakers",
                        url_prefix='/speakers')


@speakers.route('/')
class Speakers(MethodView):
    @output(SpeakersSchema)
    def get(self):
        return get_speakers()


@speakers.route('/volume/<string:name>')
class Volume(MethodView):
    @output(VolumeSchema)
    def get(self, name: str):
        vol = get_volume(name)
        return {"volume": vol}

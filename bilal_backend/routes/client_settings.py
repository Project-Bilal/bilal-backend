from apiflask import APIBlueprint, input, abort, doc
from flask.views import MethodView
from bilal_backend.libs import settings_handler as handler
from bilal_backend.spec.schemas import LocationSchema, CalculationSchema, AudioSchema, SpeakerSchema, \
    VolumeSchema

settings = APIBlueprint(import_name="User Settings",
                        name="User Settings",
                        tag="User Settings",
                        url_prefix='/settings')


@settings.route('/location')
class Location(MethodView):
    @doc(responses=[200, 412])
    def get(self):
        resp = handler.get_user_location()
        if not resp:
            abort(status_code=412, message="No Location saved")
        return resp

    @input(LocationSchema)
    @doc(responses=[200])
    def put(self, data):
        lat = data.get('lat')
        long = data.get('long')
        address = data.get('address')
        handler.set_user_location(lat, long, address)
        return 'success'


@settings.route('/calc')
class Calculation(MethodView):
    @doc(responses=[200, 412])
    def get(self):
        resp = handler.get_user_calculation()
        if not resp:
            abort(status_code=412, message="No calculation method saved")
        return resp

    @input(CalculationSchema)
    @doc(responses=[200])
    def put(self, data):
        handler.set_user_calculation(data.get('calculation'))
        return 'success'


@settings.route('/speaker')
class Speaker(MethodView):
    @doc(responses=[200, 412])
    def get(self):
        resp = handler.get_speaker()
        if not resp:
            abort(status_code=412, message="No calculation method saved")
        return resp

    @input(SpeakerSchema)
    @doc(responses=[200])
    def put(self, data):
        handler.set_speaker(data)
        return 'success'


@settings.route('/volume')
class Volume(MethodView):
    @doc(responses=[200, 412])
    def get(self):
        resp = handler.get_volume()
        if not resp:
            abort(status_code=412, message="No volume level saved")
        return resp

    @input(VolumeSchema)
    @doc(responses=[200])
    def put(self, volume: int):
        handler.set_volume(volume)
        return 'success'


@settings.delete('/reset')
@doc(responses=[200])
def reset():
    handler.reset()
    return 'success'

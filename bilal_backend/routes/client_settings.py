from apiflask import APIBlueprint, Schema, input, output, abort, fields
from flask.views import MethodView
from bilal_backend.libs import settings_handler as handler
from bilal_backend.spec.schemas import LocationSchema, CalculationSchema, AthanSchema, SpeakerSchema, VolumeSchema

settings = APIBlueprint(import_name="User Settings",
                        name="User Settings",
                        tag="User Settings",
                        url_prefix='/settings')


@settings.route('/location')
class Location(MethodView):
    def get(self):
        handler.get_user_location()

    @input(LocationSchema)
    def put(self, data):
        location = {
            'lat': data.get('lat'),
            'long': data.get('long'),
        }
        handler.set_user_location(location)
        return 'success'


@settings.route('/calc')
class Calculation(MethodView):
    def get(self):
        return handler.get_user_calculation()

    @input(CalculationSchema)
    def put(self, calc: str):
        handler.set_user_calculation(calc)
        return 'success'


@settings.route('/speaker')
class Speaker(MethodView):
    def get(self):
        return handler.get_speaker_name()

    @input(SpeakerSchema)
    def put(self, name: str):
        handler.set_speaker_name(name)
        return 'success'


@settings.route('/volume')
class Volume(MethodView):
    def get(self):
        return handler.get_speaker_volume()

    @input(VolumeSchema)
    def put(self, volume: int):
        handler.set_speaker_volume(volume)
        return 'success'


@settings.route('/athan')
class Athan(MethodView):
    def get(self):
        return handler.get_user_athan()

    @input(AthanSchema)
    def put(self, data):
        handler.set_user_athan(data.get('athan'))
        return 'success'


@settings.route('/fajir-athan')
class FajirAthan(MethodView):
    def get(self):
        handler.get_user_fajir_athan()

    @input(AthanSchema)
    def put(self, data):
        handler.set_user_fajir_athan(data.get('athan'))
        return 'success'


@settings.delete('/reset')
def reset():
    handler.reset()
    return 'success'

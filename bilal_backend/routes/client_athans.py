from apiflask import APIBlueprint, abort, input
from flask.views import MethodView
from bilal_backend.utils.audio_ids import audio
from bilal_backend.libs import athans_handler as handlers
from bilal_backend.spec.schemas import AudioSchema

athans = APIBlueprint(import_name="Athans", name="Athans", tag="Athan", url_prefix='/athans')


@athans.get('/')
def get_athans():
    return audio


@athans.route('/fajir')
class FajirAthan(MethodView):
    def get(self):
        resp = handlers.get_fajir_athan()
        if not resp:
            abort(status_code=412, message="No fajir audio id saved")
        return resp

    @input(AudioSchema)
    def put(self, audio_id):
        handlers.set_fajir_athan(audio_id)
        return 'success'


@athans.route('/dhuhr')
class DhuhrAthan(MethodView):
    def get(self):
        resp = handlers.get_dhuhr_athan()
        if not resp:
            abort(status_code=412, message="No dhuhr audio id saved")
        return resp

    @input(AudioSchema)
    def put(self, audio_id):
        handlers.set_dhuhr_athan(audio_id)
        return 'success'


@athans.route('/asr')
class AsrAthan(MethodView):
    def get(self):
        resp = handlers.get_asr_athan()
        if not resp:
            abort(status_code=412, message="No asr audio id saved")
        return resp

    @input(AudioSchema)
    def put(self, audio_id):
        handlers.set_asr_athan(audio_id)
        return 'success'


@athans.route('/mughrib')
class MughribAthan(MethodView):
    def get(self):
        resp = handlers.get_mughrib_athan()
        if not resp:
            abort(status_code=412, message="No mughrib audio id saved")
        return resp

    @input(AudioSchema)
    def put(self, audio_id):
        handlers.set_mughrib_athan(audio_id)
        return 'success'


@athans.route('/isha')
class IshaAthan(MethodView):
    def get(self):
        resp = handlers.get_isha_athan()
        if not resp:
            abort(status_code=412, message="No isha audio id saved")
        return resp

    @input(AudioSchema)
    def put(self, audio_id):
        handlers.set_isha_athan(audio_id)
        return 'success'


@athans.route('/notification')
class NotificationAthan(MethodView):
    def get(self):
        resp = handlers.get_notification()
        if not resp:
            abort(status_code=412, message="No notication audio id saved")
        return resp

    @input(AudioSchema)
    def put(self, audio_id):
        handlers.set_isha_athan(audio_id)
        return 'success'

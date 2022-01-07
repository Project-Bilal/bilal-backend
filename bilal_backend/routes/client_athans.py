from apiflask import APIBlueprint, abort, input
from flask.views import MethodView
from bilal_backend.utils.audio_ids import audio
from bilal_backend.libs import athans_handler as handlers
from bilal_backend.spec.schemas import AudioSchema
from bilal_backend.libs.constants import PrayerNames, SUCCESS

athans = APIBlueprint(import_name="Athans", name="Athans", tag="Athan", url_prefix='/athans')


@athans.get('/')
def get_athans():
    return audio


@athans.route(f'/{PrayerNames.FAJR}')
class FajrAthan(MethodView):
    def get(self):
        resp = handlers.get_athan(PrayerNames.FAJR)
        if not resp:
            abort(status_code=412, message="No fajr audio id saved")
        return resp

    @input(AudioSchema)
    def put(self, audio_id):
        handlers.set_athan(PrayerNames.FAJR, audio_id)
        return SUCCESS


@athans.route(f'/{PrayerNames.DHUHR}')
class DhuhrAthan(MethodView):
    def get(self):
        resp = handlers.get_athan(PrayerNames.DHUHR)
        if not resp:
            abort(status_code=412, message="No dhuhr audio id saved")
        return resp

    @input(AudioSchema)
    def put(self, audio_id):
        handlers.set_athan(PrayerNames.DHUHR, audio_id)
        return SUCCESS


@athans.route(f'/{PrayerNames.ASR}')
class AsrAthan(MethodView):
    def get(self):
        resp = handlers.get_athan(PrayerNames.ASR)
        if not resp:
            abort(status_code=412, message="No asr audio id saved")
        return resp

    @input(AudioSchema)
    def put(self, audio_id):
        handlers.set_athan(PrayerNames.ASR, audio_id)
        return SUCCESS


@athans.route(f'/{PrayerNames.MAGHRIB}')
class MaghribAthan(MethodView):
    def get(self):
        resp = handlers.get_athan(PrayerNames.MAGHRIB)
        if not resp:
            abort(status_code=412, message="No maghrib audio id saved")
        return resp

    @input(AudioSchema)
    def put(self, audio_id):
        handlers.set_athan(PrayerNames.MAGHRIB, audio_id)
        return SUCCESS


@athans.route(f'/{PrayerNames.ISHA}')
class IshaAthan(MethodView):
    def get(self):
        resp = handlers.get_athan(PrayerNames.ISHA)
        if not resp:
            abort(status_code=412, message="No isha audio id saved")
        return resp

    @input(AudioSchema)
    def put(self, audio_id):
        handlers.set_athan(PrayerNames.ISHA, audio_id)
        return SUCCESS


@athans.route('/notification')
class NotificationAthan(MethodView):
    def get(self):
        resp = handlers.get_athan('notification')
        if not resp:
            abort(status_code=412, message="No notication audio id saved")
        return resp

    @input(AudioSchema)
    def put(self, audio_id):
        handlers.set_athan('notification', audio_id)
        return SUCCESS


@athans.route('/schedule')
class ScheduleAthan(MethodView):
    def get(self):
        resp = handlers.schedule_notifications()
        if not resp:
            abort(status_code=412, message="Did not schedule the notifications")
        return resp

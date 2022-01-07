from apiflask import APIBlueprint, output, input, abort
from apiflask import abort
from flask.views import MethodView
from bilal_backend.libs.chromecast_handler import (
    get_speakers,
    play_sound,
    test_sound,
    play_notification,
)
from bilal_backend.spec.schemas import (
    SpeakersSchema,
    PlayedSchema,
    PlaySchema,
    TestSoundSchema,
)

speakers = APIBlueprint(
    import_name="Speaker", name="Speakers", tag="Speakers", url_prefix="/speakers"
)


@speakers.route("/")
class Speakers(MethodView):
    @output(SpeakersSchema)
    def get(self):
        return get_speakers()


@speakers.route("/play")
class PlaySound(MethodView):
    @input(PlaySchema)
    @output(PlayedSchema)
    def post(self, data):
        audio_id = data["audio_id"]
        audio_title = data["audio_title"] if "audio_title" in data else None
        return play_sound(audio_id=audio_id, audio_title=audio_title)


@speakers.route("/play/notification/<string:notification>")
class PlayNotification(MethodView):
    @output(PlayedSchema)
    def get(self, notification):
        response = play_notification(notification=notification)
        if not response:
            abort(status_code=412, message="Notification not played")
        return response


@speakers.route("/test")
class TestSound(MethodView):
    @input(TestSoundSchema)
    @output(PlayedSchema)
    def post(self, data):
        return test_sound(data)

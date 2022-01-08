from apiflask import APIBlueprint, output, input, abort
from apiflask import abort
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
@output(SpeakersSchema)
def get_speakers():
    return get_speakers()


@speakers.post("/play")
@input(PlaySchema)
@output(PlayedSchema)
def play_athan(data):
    audio_id = data["audio_id"]
    audio_title = data["audio_title"] if "audio_title" in data else None
    return play_sound(audio_id=audio_id, audio_title=audio_title)


@speakers.get("/play/notification/<string:notification>")
@output(PlayedSchema)
def play_notification(notification):
    response = play_notification(notification=notification)
    if not response:
        abort(status_code=412, message="Notification not played")
    return response


@speakers.post("/test")
@input(TestSoundSchema)
@output(PlayedSchema)
def test_sound(self, data):
    return test_sound(data)

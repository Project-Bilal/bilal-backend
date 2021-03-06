from apiflask import APIBlueprint, output, input
from apiflask import abort
from bilal_backend.libs.chromecast_handler import (
    get_speakers,
    test_sound,
    play_notification,
)
from bilal_backend.spec.schemas import (
    SpeakersSchema,
    ResponseSchema,
    TestSoundSchema,
)

speakers = APIBlueprint(
    import_name="Speaker", name="Speakers", tag="Speakers", url_prefix="/speakers"
)


@speakers.get("/")
@output(SpeakersSchema)
def get_speakers_on_network():
    return get_speakers()


@speakers.get("/play/<string:audio_id>/<int:vol>")
@output(ResponseSchema)
def play_notification_on_speaker(audio_id, vol):
    response = play_notification(audio_id=audio_id, vol=vol)
    if not response:
        abort(status_code=412, message="Notification not played")
    return response


@speakers.post("/test")
@input(TestSoundSchema)
@output(ResponseSchema)
def test_sound_on_speaker(data):
    return test_sound(data)

from apiflask import APIBlueprint, abort
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
@speakers.output(SpeakersSchema)
def get_speakers_on_network():
    return get_speakers()


@speakers.get("/play/<string:audio_id>/<int:vol>")
@speakers.output(ResponseSchema)
def play_notification_on_speaker(audio_id, vol):
    response = play_notification(audio_id=audio_id, vol=vol)
    if not response:
        abort(status_code=412, message="Notification not played")
    return response


@speakers.post("/test")
@speakers.input(TestSoundSchema)
@speakers.output(ResponseSchema)
def test_sound_on_speaker(data):
    return test_sound(data)

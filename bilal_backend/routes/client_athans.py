from apiflask import APIBlueprint, output
from bilal_backend.utils.audio_ids import audio

athans = APIBlueprint(import_name="Athans", name="Athans", tag="Athan", url_prefix='/athans')


@athans.get('/')
def get_athans():
    return audio

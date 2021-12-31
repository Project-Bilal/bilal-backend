from apiflask import APIBlueprint

speakers = APIBlueprint(import_name="Speaker",
                        name="Speakers",
                        tag="Speakers",
                        url_prefix='/speakers')


@speakers.get('/')
async def get_speakers():
    pass

from apiflask import APIBlueprint, output

athans = APIBlueprint(import_name="Athans", name="Athans", tag="Athan", url_prefix='/athans')


@athans.get('/')
async def get_athans():
    pass

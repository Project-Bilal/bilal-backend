from apiflask import APIBlueprint, output
import geocoder

athans = APIBlueprint(import_name="Athans", name="Athans", tag="Athan", url_prefix='/athans')


@athans.get('/')
def get_athans():

    return "success"

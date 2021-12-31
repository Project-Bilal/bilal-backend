from bilal_backend.libs import settings

from apiflask import APIBlueprint

user_settings = APIBlueprint(import_name="User Settings", name="User Settings", tag="User Settings",
                                         url_prefix='/settings')


@user_settings.get('/user-location')
def get_user_location():
    return settings.get_user_location()


@user_settings.put('/user-location')
def set_user_location(lat: float, long: float):
    location = {
        'lat': lat,
        'long': long,
    }
    settings.set_user_location(location)
    return True


@user_settings.get('/user-calc')
def get_user_calculation():
    return settings.get_user_calculation()


@user_settings.put('/user-calc')
def set_user_calculation(calc: str):
    settings.set_user_calculation(calc)
    return True


@user_settings.get('/speaker')
def get_speaker():
    return settings.get_speaker_name()


@user_settings.put('/speaker')
def set_speaker(name: str):
    settings.set_speaker_name(name)
    return True


@user_settings.get('/volume')
def get_volume():
    return settings.get_speaker_volume()


@user_settings.put('/volume')
def set_volume(volume: int):
    settings.set_speaker_volume(volume)
    return True


@user_settings.get('/athan')
def get_athan():
    return settings.get_user_athan()


@user_settings.put('/athan')
def set_athan(athan: str):
    settings.set_user_athan(athan)
    return True


@user_settings.get('/fajir-athan')
def get_fajir_athan():
    settings.get_user_fajir_athan()


@user_settings.put('/fajir-athan')
def set_fajir_athan(athan: str):
    settings.set_user_fajir_athan(athan)


@user_settings.delete('/reset')
def reset():
    settings.reset()
    return True

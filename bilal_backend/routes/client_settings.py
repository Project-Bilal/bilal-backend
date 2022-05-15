from apiflask import APIBlueprint, abort, doc, input
from bilal_backend.spec.schemas import UserSettings
from bilal_backend.scripts.schedule_notifications import (
    del_notifications,
    sched_notifications,
)
from bilal_backend.libs.constants import SUCCESS
from bilal_backend.libs import settings_handler as handler

settings = APIBlueprint(
    import_name="User Settings",
    name="User Settings",
    tag="User Settings",
    url_prefix="/settings",
)


@settings.delete("/reset")
@doc(responses=[200])
def reset():
    handler.reset()
    del_notifications()
    return SUCCESS


@settings.get("/all")
@doc(responses=[200])
def get_all():
    resp = handler.get_all()
    if not resp:
        abort(status_code=412, message="No data set!")
    return resp


@settings.post("/all")
@input(UserSettings)
@doc(responses=[200])
def set_all(data):
    user_settings = data.get("user_settings")
    resp = handler.set_all(user_settings)
    if not resp:
        abort(status_code=500, message="Error saving user settings")
    print(sched_notifications())
    return SUCCESS


@settings.get("/update")
@doc(responses=[200])
def update():
    resp = handler.update()
    if not resp:
        abort(status_code=412, message="Failed to update!")
    return SUCCESS

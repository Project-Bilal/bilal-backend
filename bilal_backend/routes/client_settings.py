from apiflask import APIBlueprint, abort, doc
from bilal_backend.scripts.schedule_notifications import del_notifications
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

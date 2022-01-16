from apiflask import APIBlueprint, input, abort, doc
from flask.views import MethodView
from bilal_backend.scripts.schedule_notifications import sched_notifications
from bilal_backend.libs.constants import SUCCESS
from bilal_backend.libs import settings_handler as handler
from bilal_backend.spec.schemas import (
    LocationSchema,
    SpeakerSchema,
)

settings = APIBlueprint(
    import_name="User Settings",
    name="User Settings",
    tag="User Settings",
    url_prefix="/settings",
)


@settings.route("/location")
class Location(MethodView):
    @doc(responses=[200, 412])
    def get(self):
        resp = handler.get_user_location()
        if not resp:
            abort(status_code=412, message="No Location saved")
        return resp

    @input(LocationSchema)
    @doc(responses=[200])
    def put(self, data):
        lat = data.get('lat')
        long = data.get('long')
        address = data.get('address')
        resp = handler.set_user_location(lat, long, address)
        if not resp:
            abort(status_code=404, message='Invalid Lat/Long')
        print(sched_notifications())
        return SUCCESS


@settings.get("/calculation")
def get_calculation():
    resp = handler.get_user_calculation()
    if not resp:
        abort(status_code=412, message="No calculation method saved")
    return resp


@settings.put("/method/<string:method>")
def set_method(method):
    handler.set_method(method)
    print(sched_notifications())
    return SUCCESS


@settings.put("/jurisprudence/<string:jurisprudence>")
def set_jurisprudence(jurisprudence):
    handler.set_jurisprudence(jurisprudence)
    print(sched_notifications())
    return SUCCESS


@settings.route("/speaker")
class Speaker(MethodView):
    @doc(responses=[200, 412])
    def get(self):
        resp = handler.get_speaker()
        if not resp:
            abort(status_code=412, message="No calculation method saved")
        return resp

    @input(SpeakerSchema)
    @doc(responses=[200])
    def put(self, data):
        handler.set_speaker(data)
        return SUCCESS


@settings.delete("/reset")
@doc(responses=[200])
def reset():
    handler.reset()
    return SUCCESS


@settings.get("/all")
@doc(responses=[200])
def get_all():
    resp = handler.get_all()
    if not resp:
        abort(status_code=412, message="No data set!")
    return resp

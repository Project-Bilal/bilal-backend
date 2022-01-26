from apiflask import APIBlueprint, abort

from bilal_backend.scripts.schedule_notifications import sched_notifications

athans = APIBlueprint(import_name="Athans", name="Athans", tag="Athan", url_prefix='/athans')


@athans.get('/schedule')
def schedule_notifications():
    if 'ERROR' in sched_notifications():
        abort(status_code=412, message="Did not schedule the notifications")
    return "Notifications scheduled"

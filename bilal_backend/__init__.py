from bilal_backend.routes import add_routes
from bilal_backend.scripts.schedule_notifications import (
    sched_notifications,
    add_notification_scheduler,
)
from bilal_backend.db.LightDB import LightDB
from bilal_backend.libs.constants import DATA_FILE
from apiflask import APIFlask
from flask_cors import CORS


app = APIFlask(__name__, docs_path="/", title="Project Bilal")

add_routes(app)
CORS(app)

# initialize the db
LightDB(DATA_FILE)

# add cronjob that schedules the notifications
add_notification_scheduler()

# schedule the initial notifications
sched_notifications()

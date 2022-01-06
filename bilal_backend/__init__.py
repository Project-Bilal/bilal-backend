from bilal_backend.routes import add_routes
from bilal_backend.scripts.schedule_notifications import sched_notifications, add_notification_scheduler
from apiflask import APIFlask
from flask_cors import CORS


app = APIFlask(__name__, docs_path='/', title="Project Bilal")
    
add_routes(app)
CORS(app)

# add cronjob that schedules the notifications
add_notification_scheduler()
# schedule the initial notifications
sched_notifications()

# TODO run script to add prayer timers/cron jobs
# TODO Check if db has location and calc data
# TODO If exists, run scheduler

# TODO if not exists
# TODO Run script once both calc and location exists

from bilal_backend.routes import add_routes
from apiflask import APIFlask
from flask_cors import CORS

app = APIFlask(__name__, docs_path='/', title="Project Bilal")
CORS(app)
add_routes(app)

# TODO run script to add prayer timers/cron jobs
# TODO Check if db has location and calc data
# TODO If exists, run scheduler

# TODO if not exists
# TODO Run script once both calc and location exists

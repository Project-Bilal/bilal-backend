from bilal_backend.routes import add_routes
from apiflask import APIFlask

app = APIFlask(__name__, docs_path='/')
add_routes(app)

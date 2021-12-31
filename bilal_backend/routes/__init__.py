from bilal_backend.routes.client_athans import athans
from bilal_backend.routes.client_prayers import prayer_times
from bilal_backend.routes.client_settings import settings
from bilal_backend.routes.client_speakers import speakers
from bilal_backend.routes.client_test_sound import test


def add_routes(app):
    app.register_blueprint(athans)
    app.register_blueprint(prayer_times)
    app.register_blueprint(test)
    app.register_blueprint(speakers)
    app.register_blueprint(settings)

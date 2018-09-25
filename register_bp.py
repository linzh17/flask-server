
from server_app.api import api as api_bp

def register(app):
    app.register_blueprint(api_bp)
    return app

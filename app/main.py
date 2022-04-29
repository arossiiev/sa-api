from flask_cors import CORS

from app.container import Container
from app.views import setup_views


def create_app():
    container = Container()

    app = container.app()
    app.container = container

    setup_views(container)

    # app = CORS(app, resources=r'/api/*')
    return app



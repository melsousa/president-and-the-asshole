from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    with app.app_context():
        # implementar arquivos de rotas
        from president.infrastructure.rooms.controllers.RoomController import RoomController
    return app

app = create_app()

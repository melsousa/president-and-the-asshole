from flask import Flask

app = Flask(__name__)

from president.infrastructure.rooms.controllers.RoomController import RoomController

# def create_app():
#     app = Flask(__name__, instance_relative_config=True)

#     with app.app_context():
#         # implementar arquivos de rotas
#         from president.infrastructure.rooms.controllers.RoomController import RoomController
#     return app

# app = create_app()

app.run(debug=True)

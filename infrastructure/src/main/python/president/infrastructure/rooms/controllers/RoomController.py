from main import app
from flask import request
from .........application.src.main.python.president.application.usecase.room.create.CreateRoomUseCaseImpl import CreateRoomUseCaseImpl
from ..repository.RoomInMemoryRepository import RoomInMemoryRepository

class RoomController:

    @app.route("rooms", methods = ['POST'])
    def createRoom():
        anIn =  request.get_json()

        useCase = CreateRoomUseCaseImpl(RoomInMemoryRepository())
        
        return useCase.execute(anIn)
    
    @app.route("rooms/<uuid:roomId>", methods = ['GET'])
    def retrieveRoomById(roomId):
        useCase = 
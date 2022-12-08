from president.main import app
from flask import request
from .........application.src.main.python.president.application.usecase.room.create.CreateRoomUseCaseImpl import CreateRoomUseCaseImpl
from ..repository.RoomInMemoryRepository import RoomInMemoryRepository
from .........application.src.main.python.president.application.usecase.room.retrieve.by.id.RetrieveRoomByIdUseCaseImpl import RetrieveRoomByIdUseCaseImpl
from .........core.src.main.python.president.domain.valueObject.identifier.RoomId import RoomId

class RoomController:

    @app.route("rooms", methods = ['POST'])
    def createRoom():
        anIn =  request.get_json()

        useCase = CreateRoomUseCaseImpl(RoomInMemoryRepository())
        
        return useCase.execute(anIn)
    
    @app.route("rooms/<uuid:roomId>", methods = ['GET'])
    def retrieveRoomById(roomId):
        useCase = RetrieveRoomByIdUseCaseImpl(RoomInMemoryRepository())

        return useCase.execute(RoomId.of(roomId))
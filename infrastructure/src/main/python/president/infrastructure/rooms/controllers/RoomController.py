from main import app
from flask import request

class RoomController:

    @app.route("rooms", methods = ['POST'])
    def createRoom():
        anIn =  request.get_json()

        '''
        Implementação de repository
        '''
        pass
    
    @app.route("rooms/<uuid:roomId>", methods = ['GET'])
    def retrieveRoomById(id):
        '''
        Implementação de repository
        '''
        pass
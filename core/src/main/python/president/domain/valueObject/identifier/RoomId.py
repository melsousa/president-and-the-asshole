import uuid
from BaseId import BaseId

class RoomId(BaseId):
    def __init__(self, value:uuid):
        super().__init__(value)
        
    @staticmethod
    def RoomId():
        return RoomId(uuid.uuid4()) # retornar um novo id
    
    def RoomId(value:uuid): # retornar um id já existente
        return RoomId(value)
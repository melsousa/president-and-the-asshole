import uuid
from BaseId import BaseId


class RoomId(BaseId):
    def __init__(self, value: uuid):
        super().__init__(value)

    @staticmethod
    def ofRoomId():
        return RoomId(uuid.uuid4())  # retornar um novo id

    @staticmethod
    def of(value: uuid):  # retornar um id já existente
        return RoomId(value)

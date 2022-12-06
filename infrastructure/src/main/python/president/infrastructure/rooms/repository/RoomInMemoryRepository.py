from .........core.src.main.python.president.domain.entity.Room import Room
from .........core.src.main.python.president.domain.valueObject.identifier.RoomId import RoomId
from .........core.src.main.python.president.domain.repository.RoomRepository import RoomRepository

class RoomInMemoryRepository(RoomRepository):
    
    ROOMS = {}

    def save(self, aRoom:Room):
        self.ROOMS[aRoom.roomId()] = aRoom
        return aRoom
    
    def delete(self, anId:RoomId):
        self.ROOMS.pop(anId.getValue())

    def getById(self, anId: RoomId):
        return self.ROOMS.get(anId.getValue())
    
    def getByLink(self, aLink: str):
        return None
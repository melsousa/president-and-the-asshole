from ..........core.src.main.python.president.domain.entity.Room import Room

class CreateRoomOut():
    def __init__(self, roomId, link, status):
        self.roomId = roomId
        self.link = link
        self.status = status

    # fazer gets e sets
    @property
    def roomId(self):
        return self.roomId
    
    @roomId.setter
    def roomId(self, roomId):
        self.roomId = roomId
    
    @property
    def link(self):
        return self.link
    
    @link.setter
    def link(self, link):
        self.link = link
    
    @property
    def status(self):
        return self.status
    
    @status.setter
    def status(self, status):
        self.status = status

    def CreateRoomOutOf(aRoom:Room):
        return CreateRoomOut(aRoom.roomId(), aRoom.roomLink(), aRoom.status)
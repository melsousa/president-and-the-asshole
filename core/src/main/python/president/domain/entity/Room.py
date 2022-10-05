from valueObject.AcessConfig import AcessConfig
from valueObject.identifier.PlayerId import PlayerId
from valueObject.identifier.RoomId import RoomId
from valueObject.RoomLink import RoomLink


class Room(AcessConfig):
    roomId: RoomId
    ownerId: PlayerId
    roomLink: RoomLink
    acessConfig: AcessConfig
    
    def __init__(self, roomId:RoomId, ownerId:PlayerId, roomLink:RoomLink, acessConfig:AcessConfig):
        self.roomId = roomId
        self.ownerId = ownerId
        self.roomLink = roomLink
        self.acessConfig = acessConfig
    
    @staticmethod
    def RoomOf(ownerId:PlayerId, acessConfig:AcessConfig):
        #....

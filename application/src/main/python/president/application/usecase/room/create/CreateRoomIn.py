#import AcessConfig
from ..........core.src.main.python.president.domain.valueObject.AcessConfig import AcessConfig
from ..........core.src.main.python.president.domain.entity.Room import Room
from ..........core.src.main.python.president.domain.entity.Player import Player

class CreateRoomIn():
    def __init__(self, nickName, visibility: AcessConfig.Visibility, maxPlayers):
        self.nickName = nickName
        self.visibility = visibility
        self.maxPlayers = maxPlayers
    
    @property
    def nickName(self):
        return self.nickName
    
    @nickName.setter
    def nickName(self, nickName):
        self.nickName = nickName
    
    @property
    def visibility(self):
        return self.visibility
    
    @visibility.setter
    def visibility(self, visibility:AcessConfig.Visibility):
        self.visibility = visibility
    
    @property
    def maxPlayers(self):
        return self.maxPlayers
    
    @maxPlayers.setter
    def maxPlayers(self, maxPLayers):
        self.maxPlayers = maxPLayers
    

    def toRoom(self):
        return Room.ofRoom(
            Player.ofPlayer(self.nickName), AcessConfig.of(self.maxPlayers, self.visibility)
        )

    

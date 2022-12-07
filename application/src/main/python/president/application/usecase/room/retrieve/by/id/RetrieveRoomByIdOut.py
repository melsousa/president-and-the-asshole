from ............core.src.main.python.president.domain.valueObject.AcessConfig import AcessConfig
from ............core.src.main.python.president.domain.entity.Room import Room
class RetrieveRoomByIdOut():
    def __init__(self, link, status, visibility:AcessConfig.visibility):
        self.link = link
        self.status = status
        self.visibility = visibility
    
    @property
    def link(self):
        return self.link
    
    @link.setter
    def link(self, link):
        self.link = link
    
    @property
    def visibility(self):
        return self.visibility
    
    @visibility.setter
    def visibility(self, visibility:AcessConfig.Visibility):
        self.visibility = visibility
    
    @property
    def status(self):
        return self.status
    
    @status.setter
    def status(self, status):
        self.status = status
    
    def of(aRoom:Room):
        RetrieveRoomByIdOut(aRoom.roomLink(), aRoom.status, aRoom.acessConfig())
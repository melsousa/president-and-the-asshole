from abc import ABC, abstractmethod

from ..entity.Room import Room, RoomId

class RoomRepository(ABC):
    
    @abstractmethod
    def save(aRoom:Room):
        pass

    @abstractmethod
    def delete(anId:RoomId):
        pass

    @abstractmethod
    def getById(anId:RoomId):
        pass

    @abstractmethod
    def getByLink(aLink:str):
        pass

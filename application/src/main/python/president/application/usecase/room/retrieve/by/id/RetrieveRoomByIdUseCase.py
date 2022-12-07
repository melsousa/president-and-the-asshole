from abc import ABC, abstractmethod
from ............core.src.main.python.president.domain.valueObject.identifier.RoomId import RoomId

class RetrieveRoomByIdUseCase(ABC):

    @abstractmethod
    def execute(anIn:RoomId):
        pass
from abc import ABC, abstractmethod
#importar RoomID

class RetrieveRoomByIdUseCase(ABC):

    @abstractmethod
    def execute(anIn:RoomId):
        pass
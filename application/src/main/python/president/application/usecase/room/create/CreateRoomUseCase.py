from abc import ABC, abstractmethod
from CreateRoomIn import CreateRoomIn

class CreateRoomUseCase(ABC):

    @abstractmethod
    def execute(anIn:CreateRoomIn):
        pass
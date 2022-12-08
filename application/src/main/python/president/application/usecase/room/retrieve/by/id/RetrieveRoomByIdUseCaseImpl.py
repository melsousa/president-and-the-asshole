from ............core.src.main.python.president.domain.valueObject.identifier.RoomId import RoomId
from ............core.src.main.python.president.domain.repository.RoomRepository import RoomRepository
from .RetrieveRoomByIdUseCase import RetrieveRoomByIdUseCase
from .RetrieveRoomByIdOut import RetrieveRoomByIdOut

class RetrieveRoomByIdUseCaseImpl(RetrieveRoomByIdUseCase):
    
    repository:RoomRepository

    def __init__(self, repository):
        super().__init__()
        self.repository = repository
    
    def execute(self, anIn: RoomId):
        return RetrieveRoomByIdOut.of(self.repository.getById(anIn))


from CreateRoomUseCase import CreateRoomUseCase
from CreateRoomIn import CreateRoomIn
from ..........core.src.main.python.president.domain.repository.RoomRepository import RoomRepository
from CreateRoomOut import CreateRoomOut

class CreateRoomUseCaseImpl(CreateRoomUseCase):

    repository:RoomRepository

    def __init__(self, repository:RoomRepository):
        self.repository = repository
    
    def execute(self, anIn: CreateRoomIn):
        return CreateRoomOut.CreateRoomOutOf(self.repository.save(anIn.toRoom()))
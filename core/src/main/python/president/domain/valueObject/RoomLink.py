import uuid
from ValueObject import ValueObject

class RoomLink(ValueObject):
    value = uuid.uuid4()
    
    def __init__(self, value):
        self.value = value
    
    @staticmethod
    def ofRoomLink():
        return RoomLink(uuid.uuid4())
    
    def value(self):
        return self.value
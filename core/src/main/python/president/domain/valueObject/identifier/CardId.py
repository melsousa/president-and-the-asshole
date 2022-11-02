from BaseId import BaseId
import uuid

class CardId(BaseId):
    def __init__(self, value: uuid.UUID):
        super().__init__(value)

    def ofCardId():
        return CardId(uuid.uuid4)
    
    def of(value: uuid.UUID):
        return CardId(value)
from hmac import new
import uuid
from BaseId import BaseId


class CardId(BaseId):
    def __init__(self, value: uuid):
        super().__init__(value)


    @staticmethod
    def ofCardId():  # retornar um novo id
        return CardId(uuid.uuid4())

    @staticmethod
    def of(value: uuid):  # retornar um id já existente
        return CardId(value)

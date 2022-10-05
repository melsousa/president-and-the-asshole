import uuid

from BaseId import BaseId


class PlayerId(BaseId):
    def __init__(self, value: uuid):
        super().__init__(value)

    @staticmethod
    def PlayerId():
        return PlayerId(uuid.uuid4())  # retornar um novo id

    def PlayerId(value: uuid):  # retornar um id já existente
        return PlayerId(value)

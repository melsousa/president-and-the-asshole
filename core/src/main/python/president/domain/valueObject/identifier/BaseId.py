from abc import ABC
from asyncio.windows_events import NULL
import uuid

from valueObject.ValueObject import ValueObject


class BaseId(ValueObject, ABC):
    # UIID4 é mais seguro pois não cria um id baseado no endreço da rede
    value = uuid.uuid4()

    def __init__(self, value):
        self.value = value

    def value(self):
        return self.value

    def __eq__(self, Object):
        if self.value == Object.value:
            return True
        if Object.value == NULL:  # faltando implementação
            return False

        # BaseId
        # return value.__eq__(Object.value)

    def hashCode(self):
        pass
        # Objects.hashCode(self)

from abc import ABC
from asyncio.windows_events import NULL
from pydoc import classname
import uuid

from valueObject.ValueObject import ValueObject


class BaseId(ValueObject, ABC):
    # UIID4 é mais seguro pois não cria um id baseado no endreço da rede
    value = uuid.uuid4()

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value.__str__()

    def __eq__(self, o):
        if self.value == o:
            return True
        if o == NULL or self.__class__.__name__ != o.__class__.__name__:  
            return False
        baseId = BaseId(o)
        return self.value.__eq__(baseId.value)

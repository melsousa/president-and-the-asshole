from enum import Enum
from tarfile import FIFOTYPE
from ValueObject import ValueObject

class CardValue(ValueObject, Enum):
    
    ACE = 12
    TWO = 13
    THREE = 1
    FOUR = 2
    FIVE = 3    
    SIX = 4
    SEVEN = 5
    EIGHT = 6
    NINE = 7
    TEN = 8
    JACK = 9
    QUEEN = 10
    KING = 11
    
    def __init__(self, value):
        self.value = value
    
    def value(self):
        return self.value
    
    # def compare(self, ):
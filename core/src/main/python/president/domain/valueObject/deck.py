from typing import List

from entity.Card import Card
from CardValue import CardValue
from Suit import Suit
from ValueObject import ValueObject

class Deck(ValueObject):
    
    card: List[Card] = []
   
    def __init__(self) :
        self._deck = Card[52]
        
        for i in range(0, 52, 1):
            self._deck[i] = Card.ofCard(CardValue.value()[i % 13], Suit.value()[i / 13])
    
    @property
    def _Card(self):
        return self._Card
   
    def Deckof(self):
        return Deck()
    
    
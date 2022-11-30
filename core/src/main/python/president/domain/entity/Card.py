from valueObject.CardValue import CardValue
from valueObject.Suit import Suit
from valueObject.identifier.CardId import CardId

class Card:
    cardId:CardId
    cardValue:CardValue
    suit:Suit

    def __init__(self, cardId:CardId, cardValue:CardValue, suit:Suit):
        self.cardId = cardId
        self.cardValue = cardValue
        self.suit = suit

    @staticmethod
    def ofCard(cardValue:CardValue, suit:Suit):
        return Card(CardId.of(), cardValue, suit)

    @property
    def CardId(self):
        return self.cardId
    
    @property
    def CardValue(self):
        return self.cardValue
    
    @property
    def Suit(self):
        return self.suit

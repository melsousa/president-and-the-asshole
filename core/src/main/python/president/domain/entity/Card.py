from functools import cmp_to_key

from valueObject.CardValue import CardValue
from valueObject.Suit import Suit
from valueObject.identifier.CardId import CardId
from Card import Card

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

    def getCardId(self):
        return self.cardId

    def getCardValue(self):
        return self.cardValue

    def getSuit(self):
        return self.suit
    
    def toString(self):
        return self.cardValue + " of "+ self.suit
    
    def compareTo(self, o:Card):
        return o.getCardValue().value() - self.getCardValue().value
    
    def __eq__(self, c:Card):
        return self.c == c

        


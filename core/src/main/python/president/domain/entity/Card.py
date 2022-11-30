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

    def getCardId():
        return cardId

    def getCardValue():
        return cardValue

    def getSuit():
        return suit

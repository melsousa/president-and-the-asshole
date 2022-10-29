from asyncio.windows_events import NULL
from typing import List

from valueObject.identifier.PlayerId import PlayerId
from valueObject.CardValue import CardValue
from Card import Card


class Player:

    playerId: PlayerId
    cards: List[Card] = []

    def __init__(self, playerId: PlayerId, nickName, cards: List[Card], choiceCard: Card):
        self.playerId = playerId
        self.nickName = nickName
        self.cards = cards
        self.choiceCard = choiceCard

    def ofPlayer(self, nickName):
        return Player(PlayerId.of(), nickName, [], NULL)  # ?

    def SetchoiceCard(self, card: Card):
        self.choiceCard = card

    def playerId(self):
        return self.playerId

    def nickName(self):
        return self.nickName

    def cards(self):
        return self.cards  # ?

    def choiceCard(self):
        return self.choiceCard

    # def compareto(self, o):
    #     pass

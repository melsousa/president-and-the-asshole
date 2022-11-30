from typing import List
from enum import Enum

from numpy import place

from valueObject.AcessConfig import AcessConfig
from valueObject.CardValue import CardValue
from valueObject.RoomLink import RoomLink
from valueObject.Suit import Suit
from valueObject.identifier.PlayerId import PlayerId
from valueObject.identifier.RoomId import RoomId
from valueObject.RoomLink import RoomLink
from valueObject.deck import Deck
from Card import Card
from Player import Player
from Status import Status


class Room(Enum):

    N_DECKS = 2
    roomId: RoomId
    owner: Player
    roomLink: RoomLink
    acessConfig: AcessConfig
    players: List[Player] = []
    playersToChoice: List[PlayerId] = []
    cardsToChoice: List[Card] = []

    cardsToChoice: List[Card] = []
    status: Status

    def __init__(self, roomId: RoomId, owner: Player, roomLink: RoomLink, acessConfig: AcessConfig, players: List[Player]):
        self.roomId = roomId
        self.owner = owner
        self.roomLink = roomLink
        self.acessConfig = acessConfig
        self.players = players
        self.cardsToChoice = []
        self.cardsToDeal = []

        self.status = Status.WAITING

    def dealCards(self):
        pass
        # qtyCardsOfRemove = (self.N_DECKS * 52) % self.players.__len__()
        # card = 0
        # for i in range(0, self.N_DECKS, 1):
        #     for j in range(card:Deck.Deckof()._Card()):
        #         if card.CardValue()

    def toSorting(self):
        if self.status != Status.WAITING:
            print("Room is not waiting")  # +

    def shuffleCardsToChoice(self):
        if self.players.__len__() < self.acessConfig.minplayers():
            raise RuntimeError("'max players' can't be less than four!")
        
        # for 
        
    @staticmethod
    def ofRoom(ownerId: PlayerId, acessConfig: AcessConfig):
        roomId = RoomId.ofRoomId()
        roomLink = RoomLink.ofRoomLink()
        players: List[PlayerId] = []
        players.append(ownerId)

        return Room(roomId, ownerId, roomLink, acessConfig, players)

    def choiceCard(self,player:Player):
        if self.status != Status.IN_SORTING:
            pass
        
    def addPlayer(self, playerId: PlayerId):
        pass
        # if self.players.len() >= self.acessConfig.maxPlayers():
        #     raise RuntimeError("This room is full!")

        # self.players.append(playerId)

    def roomId(self):
        return self.roomId

    def ownerId(self):
        return self.ownerId

    def roomLink(self):
        return self.roomLink

    def acessConfig(self):
        return self.acessConfig

    def players(self):
        return self.players

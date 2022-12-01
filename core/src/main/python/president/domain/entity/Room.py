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

    cardsToDeal: List[Card] = []
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
    
    def initializePlayers(self, players:Player[List]):
        self.playersToChoice = [players.index(players.playerId(), 0, players.__len__())] # ?
        
    def toSorting(self):
        if self.status != Status.WAITING:
            print("Room is not waiting") # +
        
        self.shuffleCardsToChoice()
        self.status = Status.IN_SORTING
    
    def shuffleCardsToChoice(self):
        if self.players.__len__() < self.acessConfig.minplayers():
            raise RuntimeError("'max players' can't be less than four!")
        
        # for(cardValue:CardValue.):
           
    @staticmethod
    def ofRoom(owner: Player, acessConfig: AcessConfig):
        roomId = RoomId.ofRoomId()
        roomLink = RoomLink.ofRoomLink()
        players: List[PlayerId] = []
        players.append(owner)

        return Room(roomId, owner, roomLink, acessConfig, players)

    def choiceCard(self, player:Player):
        if self.status != Status.IN_SORTING:
            print("Room is not in sorting")
        
        if (self.playerToChoice.__contains__(player.playerId())): # ++
            print("Can't choice card for player "+ player.playerId().value)
        
        card = self.cardsToChoice.get(0) # está faltando código
        player.choiceCard(card)
        self.cardsToChoice.remove(card)
        self.playersToChoice.remove(player.playerId())

        return card

    def sortPlayers(self):
        if len(self.playersToChoice) == 0:
            self.players.sort(Player) # faltando códogp
            pass

    def toThrowing(self):
        if self.status != Status.IN_SORTING and self.status != Status.ROUND_FINISHED:
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

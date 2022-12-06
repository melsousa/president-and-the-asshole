from typing import List
from enum import Enum

#from numpy import place

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

        self.initializePlayers(players)

        self.status = Status.WAITING

    def dealCards(self):

        qtyCardsOfRemove = (self.N_DECKS * 52) % self.players.__len__()
        card = 0

        for i in range(0, self.N_DECKS, 1):
            for card in Deck.Deckof()._Card():
                if card.CardValue().__eq__(CardValue.THREE) and qtyCardsOfRemove > 0:  # ?
                    qtyCardsOfRemove -= 1

                self.cardsToDeal.append(card)
                # ++

        currentPlayer = 0

        for card in self.cardsToDeal:
            self.players.get(currentPlayer).addCard(card)
            currentPlayer = (currentPlayer + 1) % self.players.__len__()

    def initializePlayers(self, players: Player[List]):
        self.playersToChoice = [players.index(
            players.playerId(), 0, players.__len__())]  # ?

    def toSorting(self):
        if self.status != Status.WAITING:
            raise ValueError("Room is not waiting")

        self.shuffleCardsToChoice()
        self.status = Status.IN_SORTING

    def shuffleCardsToChoice(self):
        if self.players.__len__() < self.acessConfig.minplayers():
            raise RuntimeError("'min players' can't be less than four!")

        for cardValue in CardValue.value():
            self.cardsToChoice.append(Card.ofCard(cardValue, Suit.CLUBS))

        # ++

    @staticmethod
    def ofRoom(owner: Player, acessConfig: AcessConfig):
        roomId = RoomId.ofRoomId()
        roomLink = RoomLink.ofRoomLink()
        players: List[Player] = []
        players.append(owner)

        return Room(roomId, owner, roomLink, acessConfig, players)

    def choiceCar(self, player: Player):
        if self.status != Status.IN_SORTING:
            raise ValueError("Room is not in sorting")

        if (not (self.playerToChoice.__contains__(player.playerId()))):  # ++
            raise ValueError("Can't choice card for player " + player.playerId().value())

        card = self.cardsToChoice.get(0)  
        player.choiceCard(card)
        self.cardsToChoice.remove(card)
        self.playersToChoice.remove(player.playerId())

        return card

    def sortPlayers(self):
        if len(self.playersToChoice) == 0:
            self.players.sort(Player)  # faltando códogp
            self.toThrowing()

    def toThrowing(self):
        if self.status != Status.IN_SORTING and self.status != Status.ROUND_FINISHED:
            raise ValueError("Room is not in sorting or round finished")
        
        self.status = Status.THROWING_CARDS
    
    def toInGame(self):
        if self.status != Status.THROWING_CARDS:
            raise ValueError("Room is not throwing cards")
        
        self.status = Status.IN_GAME
        

    def addPlayer(self, player:Player):
        if self.players.__len__() >= self.acessConfig.maxPlayers():
            raise RuntimeError("This room is full!")

        self.players.append(player)
        self.playersToChoice.append(player.playerId())

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

    def cardsToDeal(self):
        # return
        pass

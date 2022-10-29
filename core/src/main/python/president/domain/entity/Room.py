from typing import List
from enum import Enum

from numpy import place
from core.src.main.python.president.domain.entity.Player import Player

from valueObject.AcessConfig import AcessConfig
from valueObject.CardValue import CardValue
from valueObject.RoomLink import RoomLink
from valueObject.Suit import Suit
from valueObject.identifier.PlayerId import PlayerId
from valueObject.identifier.RoomId import RoomId
from valueObject.RoomLink import RoomLink

from Card import Card
from Player import Player
from Status import Status


class Room(Enum):

    roomId: RoomId
    owner: Player
    roomLink: RoomLink
    acessConfig: AcessConfig
    players: List[Player] = []
    playersToChoice: List[PlayerId] = []
    cardsToChoice: List[Card] = []
    status: Status

    def __init__(self, roomId: RoomId, owner: Player, roomLink: RoomLink, acessConfig: AcessConfig, players: List[Player]):
        self.roomId = roomId
        self.owner = owner
        self.roomLink = roomLink
        self.acessConfig = acessConfig
        self.players = players
        self.cardsToChoice = [] # +
        self.status = Status.WAITING

    def toSorting(self):
        if self.status != Status.WAITING:
            print("Room is not waiting") # +
            
            
    @staticmethod
    def ofRoom(ownerId: PlayerId, acessConfig: AcessConfig):
        roomId = RoomId.ofRoomId()
        roomLink = RoomLink.ofRoomLink()
        players: List[PlayerId] = []
        players.append(ownerId)

        return Room(roomId, ownerId, roomLink, acessConfig, players)

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

    def players(self):  # ?
        return self.players

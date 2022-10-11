from typing import List
from enum import Enum

from numpy import place

from valueObject.AcessConfig import AcessConfig
from valueObject.identifier.PlayerId import PlayerId
from valueObject.identifier.RoomId import RoomId
from valueObject.RoomLink import RoomLink


class Room(Enum):

    IN_LOBY = "IN_LOBY"
    SORTING = "SORTING"
    READY = "READY"
    ROUND = "ROUND"
    ROUND_FINISHED = "ROUND_FINISHED"
    FINISHED = "FINISHED"

    roomId: RoomId
    ownerId: PlayerId
    roomLink: RoomLink
    acessConfig: AcessConfig
    players: List[PlayerId] = []

    def __init__(self, roomId: RoomId, ownerId: PlayerId, roomLink: RoomLink, acessConfig: AcessConfig, players: List[PlayerId]):
        self.roomId = roomId
        self.ownerId = ownerId
        self.roomLink = roomLink
        self.acessConfig = acessConfig
        self.players = players

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

    def players(self):
        return self.players

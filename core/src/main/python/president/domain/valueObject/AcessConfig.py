from ValueObject import ValueObject
from Visibility import Visibility
from enum import Enum


class AcessConfig(ValueObject, Visibility):

    MIN_PLAYERS = 4

    def __init__(self, maxPlayers, timeOfNextPlayer, visibility: Visibility):

        self.maxPlayers = maxPlayers
        self.timeOfNextPlayer = timeOfNextPlayer
        self.visibility = visibility 

    @staticmethod
    def ofPublic(self, maxPlayers):
        return self.of(
            maxPlayers,
            Visibility.PUBLIC
        )
    
    @staticmethod
    def ofPrivate(self, maxPlayers):
        return self.of(
            maxPlayers,
            Visibility.PRIVATE
        )
    
    @staticmethod
    def of(maxPlayers, visibility: Visibility):
        if(maxPlayers < AcessConfig.MIN_PLAYERS):
            print("Erro: 'max players' can´t be less than four")
        
        if(maxPlayers > 13):
            print("Erro: 'max players' can´t be greater than 13")
        
        return AcessConfig(maxPlayers, 15, visibility)

    def getMinPlayers():
        return AcessConfig.MIN_PLAYERS
    
    def getMaxPlayers(self):
        return self.maxPlayers
    
    def getTimeOfNextPlayer(self):
        return self.timeOfNextPlayer

    def getVisibility(self):
        return self.visibility
    
    class Visibility(Enum):
        PUBLIC = 0
        PRIVATE = 1


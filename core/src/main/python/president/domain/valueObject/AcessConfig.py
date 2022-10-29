from ValueObject import ValueObject
from Visibility import Visibility


class AcessConfig(ValueObject, Visibility):

    MIN_PLAYERS = 4

    def __init__(self, maxPlayers, timeOfNextPlayer, visibility: Visibility):

        self.maxPlayers = maxPlayers
        self.timeOfNextPlayer = timeOfNextPlayer
        self.visibility = visibility

    @staticmethod
    def ofPublicAcessConfig(maxplayers):
        return AcessConfig(maxplayers, Visibility.PUBLIC)  # ?

    @staticmethod
    def ofPrivateAcessConfig(maxplayers):
        return AcessConfig(maxplayers, Visibility.PRIVATE)

    def ofAcessConfig(maxPlayers, visibility: Visibility):
        if maxPlayers < AcessConfig.MIN_PLAYERS:
            raise RuntimeError("'max players' can't be less than four")

        if maxPlayers > 13:
            raise RuntimeError("'max players' can't be greater than 13")

        return AcessConfig(maxPlayers, 15, visibility)

    def minPlayers(self):
        return self.MIN_PLAYERS

    def maxPlayers(self):
        return self.maxPlayers

    def timeOfNextPlayer(self):
        return self.timeOfNextPlayer

    def visibility(self):
        return self.visibility

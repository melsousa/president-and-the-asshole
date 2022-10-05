from ValueObject import ValueObject


class AcessConfig(ValueObject):
    def __init__(self, minPlayers, maxPlayers, timeOfNextPlayer):
        self.minPlayers = minPlayers
        self.maxPlayers = maxPlayers
        self.timeOfNextPlayer = timeOfNextPlayer

    @staticmethod
    def AcessConfig(minPlayers, maxPlayers):
        if minPlayers < 4:
            raise RuntimeError("'min players' can't be less than 4");
        
        if minPlayers > 13:
            raise RuntimeError("'min players' can't be less than 4");
        
        if maxPlayers > 13:
            raise RuntimeError("'min players' can't be less than 4");
        
        if maxPlayers < minPlayers:
            raise RuntimeError("'min players' can't be less than 4");
        
        return AcessConfig(minPlayers, maxPlayers, 15)
    
    def minPlayers(self):
        return self.minPlayers
    
    def maxPlayers(self):
        return self.maxPlayers
    
    def timeOfNextPlayer(self):
        return self.timeOfNextPlayer
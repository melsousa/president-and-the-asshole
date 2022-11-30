import card as Card

class Deck:
    
    def _Card(self,Card):
        self._Card = Card[]
        
    @property
    def _Card(self):
        return self._Card
    
    @_Card.setter
    def Card(self, _cards):
        self._Card = _cards
        
    def _deck(self) :
        self._deck = Card[52]
        
        for i in range(0, 13):
            self._deck[i] = Card(i, "Spades")
        for i in range(13, 26):
            self._deck[i] = Card(i, "Hearts")
        for i in range(26, 39):
            self._deck[i] = Card(i, "Clubs")
        for i in range(39, 52):
            self._deck[i] = Card(i, "Diamonds")
            
    @property
    def _deck(self):
        return self._deck
    
    @_deck.setter
    def deck(self, _deck):
        self._deck = _deck
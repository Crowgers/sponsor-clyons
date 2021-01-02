import random


class Card:
    def __init__(self, suit, rank, available=True):
        self.suit = suit
        self.rank = rank
        self.available = available

    def __str__(self):
        return f"[ {self.suit} / {self.rank} ]"
        
    def get_value(self):
        if (
            self.rank == "2" or
            self.rank == "3" or
            self.rank == "4" or
            self.rank == "5" or
            self.rank == "6" or
            self.rank == "7" or
            self.rank == "8" or
            self.rank == "9" or
            self.rank == "10"
        ):
            val = int(self.rank)
        elif (self.rank == "Jack" or
              self.rank == "Queen" or
              self.rank == "King"):
            val = 10
        elif self.rank == "Ace":
            val = 11
        return val


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["HEARTS", "CLUBS", "SPADES", "DIAMONS"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
                
    def get_random_card(self):
        while True:
            index = random.randint(0,51)
            if self.cards[index].available:
                self.cards[index].available = False
                return self.cards[index]


deck = Deck()
print(deck.get_random_card())
print(deck.get_random_card())


def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    
    def __str__():
        return self.rank + 'of' + self.suit
    



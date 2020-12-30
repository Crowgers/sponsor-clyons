class Card:
    __slots__ = ["rank", "name", "suit", "value"]

    def __init__(self, the_rank, the_value, the_suit):
        self.rank = the_rank
        self.value = the_value
        self.suit = the_suit
        self.name = f"{self.rank} of {self.suit}s"

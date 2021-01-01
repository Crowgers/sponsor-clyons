class Card:
    __slots__ = ["rank", "suit", "value", "name"]

    def __init__(self, rank: str, value: int, suit: str):
        self.rank = rank
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card(rank={self.rank}, value={self.value}, suit={self.suit})"

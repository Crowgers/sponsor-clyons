class Card:
    __slots__ = ["rank", "suit", "value", "name"]

    def __init__(self, rank: str, value: int, suit: str):
        self.rank = rank
        self.value = value
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

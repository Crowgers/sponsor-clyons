# Local Application Imports
from blackjack_assignment.components.card import Card


class Player:
    def __init__(self, cards: list[Card], name: str = "Player"):
        self.hand = cards
        self.score = sum([item.value for item in self.hand])
        self.bust = False
        self.sticking = False
        self.name = name

    def __str__(self):
        return self.name

    def hit(self, card: Card):
        self.hand.append(card)
        self.score = sum([item.value for item in self.hand])

    def bust(self):
        self.bust = True

    def stick(self):
        self.sticking = True

    def show_hand(self):
        return [str(item) for item in self.hand]

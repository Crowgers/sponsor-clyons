# Application Imports
from blackjack_assignment.components.card import Card

# Types for static Type checking
Hand = list[Card]


class Player:
    """
    Player Class - will have a single
    """
    def __init__(self, cards: Hand):
        self.hand = cards
        self.score = 0
        self.sticking = False

    def hit(self, card: Card):
        self.hand.append(card)
        self.score = sum([item.value for item in self.hand])
        return self.score

    def stick(self):
        self.sticking = True
        return self.sticking

    def show_hand(self):
        return [str(item) for item in self.hand]

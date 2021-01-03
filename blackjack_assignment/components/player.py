# Local Application Imports
from blackjack_assignment.components.card import Card


class Player:
    def __init__(self, cards: list[Card]):
        self.hand: list[Card] = cards
        self.score: int = sum([item.value for item in self.hand])
        self.busted: bool = False
        self.sticking: bool = False

    def hit(self, card: Card):
        self.hand.append(card)
        self.score += card.value

    def bust(self):
        self.busted = True

    def stick(self):
        self.sticking = True

    def show_hand(self) -> list[str]:
        return [str(item) for item in self.hand]

# Local Application Imports
from blackjack_assignment.components.card import Card


class Player:
    def __init__(self, cards: list[Card]):
        self.hand: list[Card] = cards
        self.score: int = sum([item.value for item in self.hand])
        self.busted: bool = False
        self.sticking: bool = False

    def hit(self, card: Card):
        """
        Appends a card to the players deck and increments their score
        :param card: Card from Deck
        """
        self.hand.append(card)
        self.score += card.value

    def bust(self):
        """
        Modifies attribute of player which tracks if they are bust.
        """
        self.busted = True

    def stick(self):
        """
        Modifies attribute of player which tracks if they chose to stick.
        """
        self.sticking = True

    def show_hand(self) -> list[str]:
        """
        :return: string representation of the players cards.
        """
        return [str(item) for item in self.hand]

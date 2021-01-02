# Local Application Imports
from blackjack_assignment.components.card import Card
from blackjack_assignment.components.deck import Deck
from blackjack_assignment.components.player import Player


class Dealer(Player):
    def __init__(self):
        self.__deck: Deck = Deck()
        super().__init__([self.deal_card()])  # Inherit 2nd as requires deck
        self.__hidden: list[Card] = [self.deal_card()]

    def deal_card(self) -> Card:
        return self.__deck.draw_card()

    def count_hidden(self) -> int:
        return len(self.__hidden)

    def reveal_hidden(self):
        self.hit(self.__hidden.pop())

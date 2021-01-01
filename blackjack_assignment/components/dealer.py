# Local Application Imports
from blackjack_assignment.components.card import Card
from blackjack_assignment.components.deck import Deck
from blackjack_assignment.components.player import Player


class Dealer(Player):
    def __init__(self):
        self.__deck: Deck = Deck()
        # Inheritance is done after "self.__deck" to be initialised
        super().__init__([self.deal_card()], name="Dealer")
        self.__hidden: list[Card] = [self.deal_card()]

    def deal_card(self):
        return self.__deck.draw_card()

    def count_hidden(self):
        return len(self.__hidden)

    def reveal_hidden(self):
        return self.hit(self.__hidden.pop())

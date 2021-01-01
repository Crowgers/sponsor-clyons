# Application Imports
from blackjack_assignment.components.deck import Deck
from blackjack_assignment.components.player import Player


class Dealer:
    def __init__(self):
        self.__deck = Deck()
        self.__hidden = self.deal_card()
        self.hand = [self.deal_card()]
        self.score = sum([item.value for item in self.hand])
        self.player = Player([self.deal_card() for i in range(2)])

    def deal_card(self):
        return self.__deck.draw_card()

    def hit(self, first_hit=False):
        if first_hit:
            card = self.__hidden
        else:
            card = self.deal_card()
        self.hand.append(card)
        self.score = sum([item.value for item in self.hand])
        return self.score

    def show_hand(self):
        return [str(item) for item in self.hand]

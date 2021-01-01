# Application Imports
from ciaran_lyons_blackjack.components.deck import Deck


class Dealer:
    def __init__(self):
        self.__deck = Deck()
        self.__hidden = None
        self.hand = []
        self.score = sum([item.value for item in self.hand])

    def opening_deal(self):
        self.hit()
        self.__hidden = self.__deck.draw_card()
        return self.score

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

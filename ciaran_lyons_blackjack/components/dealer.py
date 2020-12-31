# Application Imports
from card import Card
from deck import Deck


class Dealer:
    def __init__(self):
        self.__deck = Deck()
        self.__score = sum([item.value for item in self.__hand])
        self.__hand = []
        self.visible_card = []

    def deal_card(self):
        return self.__deck.draw_card()

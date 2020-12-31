# Application Imports
from card import Card


class Dealer:
    def __init__(self):
        self.cards = []
        self.visible_card = ""
        self.__value_hand = 0
        self.value_hand = sum([item.value for item in self.cards])

#  Application Imports
from card import Card


class Player:
    def __init__(self):
        self.__cards = []
        self.__value_hand = 0
        self.__sticking = False  # True means player is sticking

    def hit(self, card: Card):
        self.__cards.append(card)
        self.__value_hand = sum([item.value for item in self.__cards])
        return self.__value_hand

    def stick(self):
        self.__sticking = True
        return self.__sticking

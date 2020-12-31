#  Application Imports
from card import Card


class Player:
    def __init__(self):
        self.__cards = []
        self.__score = 0
        self.__sticking = False  # True means player is sticking

    def hit(self, card: Card):
        self.__cards.append(card)
        self.__score = sum([item.value for item in self.__cards])
        return self.__score

    def stick(self):
        self.__sticking = True
        return self.__sticking

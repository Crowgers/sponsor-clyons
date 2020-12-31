# Standard Library Imports
import random

# Application Level import
from card import Card
from config import suits, rank_values


class Deck:
    def __init__(self):
        self.__cards = [  # of type list
            Card(rank, rank_values.get(rank), suit)
            for suit in suits
            for rank in rank_values.keys()
        ]

    def draw_card(self):
        choice_index = random.choice(range(len(self.__cards)))
        return self.__cards.pop(choice_index)

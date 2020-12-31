# Standard Library Imports
import random

# Application Level import
from card import Card


class Deck:
    def __init__(self):
        self.__suits = ["Heart", "Diamond", "Club", "Spade"]
        self.__rank_vals = [
            ("2", 2),
            ("3", 3),
            ("4", 4),
            ("5", 5),
            ("6", 6),
            ("7", 7),
            ("8", 8),
            ("9", 9),
            ("10", 10),
            ("JACK", 10),
            ("QUEEN", 10),
            ("KING", 10),
            ("ACE", 11)
        ]
        self.__cards = [  # of type list
            Card(rank_val[0], rank_val[1], suit)
            for suit in self.__suits
            for rank_val in self.__rank_vals
        ]

    def draw_card(self):
        choice_index = random.choice(range(len(self.__cards)))
        return self.__cards.pop(choice_index)

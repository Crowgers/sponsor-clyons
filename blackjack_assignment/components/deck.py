# Standard Library Imports
import random

# Local Application Imports
from blackjack_assignment.components.card import Card
from blackjack_assignment.components.variables import (
    num_of_decks,
    rank_values,
    suits
)


class Deck:
    def __init__(self):
        self.__cards = [
            Card(rank, rank_values.get(rank), suit)
            for suit in suits
            for rank in rank_values.keys()
            for _ in range(num_of_decks)
        ]

    def draw_card(self):
        choice_index = random.choice(range(len(self.__cards)))
        return self.__cards.pop(choice_index)

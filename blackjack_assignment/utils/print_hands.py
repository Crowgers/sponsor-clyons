from blackjack_assignment.components.dealer import Dealer
from blackjack_assignment.components.player import Player


def print_hands(dealer: Dealer, player: Player):
    print(f"\tDealer's hand: ({dealer.score}) {dealer.show_hand()} and "
          f"has {dealer.count_hidden()} face down card.")
    print(f"\tPlayer's hand: ({player.score}) "
          f"{player.show_hand()}")

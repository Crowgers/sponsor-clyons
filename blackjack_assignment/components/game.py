# Local Application Imports
from blackjack_assignment.components.dealer import Dealer
from blackjack_assignment.components.user_input import ask
from blackjack_assignment.components.player import Player


class Game:
    def __init__(self):
        print("Dealing Hands...")
        self.dealer: Dealer = Dealer()  # Dealer needs to exist first
        self.player: Player = Player(
            [self.dealer.deal_card() for _ in range(2)]
        )  # TODO:  Make the initial dealing of 2 cards more clear

    # TODO: the player turn is not immediately clear on inspection.
    def __players_turn(self):
        while not any([self.player.busted, self.player.sticking]):
            self.print_hands()
            decision = ask("Hit or Stick?", ["Hit", "Stick"])
            if decision == 0:
                self.player.hit(self.dealer.deal_card())
            else:
                self.player.stick()

            if self.player.score > 21:  # FIXME: Magic number
                self.player.bust()

    # TODO: the dealer turn is not immediately clear on inspection.
    def __dealers_turn(self):
        self.dealer.reveal_hidden()
        if not self.player.score > 21:  # FIXME: Magic number
            # Unusual but it's guaranteed to exit after finite loops
            while not self.dealer.score > 17:  # FIXME: Magic number
                print("Dealer hits...")
                self.dealer.hit(self.dealer.deal_card())
            self.print_hands()

    def print_hands(self):
        print(f"\tDealer's hand: ({self.dealer.score}) "
              f"{self.dealer.show_hand()} and "
              f"has {self.dealer.count_hidden()} hidden card(s).")
        print(f"\tPlayer's hand: ({self.player.score}) "
              f"{self.player.show_hand()}")

    def play(self):
        self.__players_turn()
        self.__dealers_turn()
        if self.player.score > 21:  # FIXME: Magic number
            print(f"Dealer ({self.dealer.score}) wins. "
                  f"Player ({self.player.score}) is bust.")
        elif self.dealer.score > 21:  # FIXME: Magic number
            print(f"Player ({self.player.score}) wins: " 
                  f"Dealer ({self.dealer.score}) is bust.")
        elif self.dealer.score > self.player.score:
            print(f"Dealer ({self.dealer.score}) wins: "
                  f"Player ({self.player.score}) < dealer")
        elif self.dealer.score < self.player.score:
            print(f"Player ({self.player.score}) wins: "
                  f"player > dealer ({self.dealer.score})")
        else:  # self.dealer.score == self.player.score ## not good rewrite
            print(f"Draw game: Player ({self.player.score}) = "
                  f"Dealer ({self.dealer.score})")
        print("Game Finished.")

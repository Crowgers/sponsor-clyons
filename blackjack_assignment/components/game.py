# Local Application Imports
from blackjack_assignment.components.dealer import Dealer
from blackjack_assignment.utils.user_input import ask
from blackjack_assignment.components.player import Player


class Game:
    def __init__(self):
        print("Dealing Hands...")
        #  Technically the game class could inherit from the dealer however
        #  inheriting from player would cause n overload of certain methods
        #  in the player class which dealer inherits from,.
        self.dealer = Dealer()  # Dealer needs to exist first
        self.player = Player([self.dealer.deal_card() for _ in range(2)])

    def __next__(self):
        return self

    def __iter__(self):
        return self

    def __players_turn(self):
        while not any([self.player.busted, self.player.sticking]):
            self.print_hands()
            decision = ask("Hit or Stick?", ["Hit", "Stick"])
            if decision == 0:
                self.player.hit(self.dealer.deal_card())
            else:
                self.player.stick()
            if self.player.score > 21:
                self.player.bust()

    def __dealers_turn(self):
        self.dealer.reveal_hidden()
        if not self.player.score > 21:
            # Unusual but it's guaranteed to exit after finite loops
            while not self.dealer.score > 17:
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
        if self.player.score > 21:
            print(f"Dealer ({self.dealer.score}) wins. "
                  f"Player ({self.player.score}) is bust.")
        elif self.dealer.score > 21:
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

# Local Application Imports
from blackjack_assignment.components.dealer import Dealer
from blackjack_assignment.utils.user_input import ask
from blackjack_assignment.components.player import Player


class Game:
    def __init__(self):
        print("Dealing Hands...")
        self.dealer = Dealer()  # Dealer needs to exist first
        self.player = Player([self.dealer.deal_card() for _ in range(2)])

    def __next__(self):
        return self

    def __iter__(self):
        return self

    def players_turn(self):
        while not self.player.busted:
            self.print_hands()
            decision = ask("Hit or Stick?", ["Hit", "Stick"])
            if self.player.score > 21:
                self.player.bust()
                break
            elif decision == 0:
                self.player.hit(self.dealer.deal_card())
            else:
                self.player.stick()
                break
        return

    def dealers_turn(self):
        # Dealers turn
        self.dealer.reveal_hidden()
        self.print_hands()
        if self.player.score < 21:
            # Unusual but it's guaranteed to exit after finite loops
            while not self.dealer.score > 17:
                self.print_hands()
                self.dealer.hit(self.dealer.deal_card())

    def print_hands(self):
        print(f"\tDealer's hand: ({self.dealer.score}) "
              f"{self.dealer.show_hand()} and "
              f"has {self.dealer.count_hidden()} face down card.")
        print(f"\tPlayer's hand: ({self.player.score}) "
              f"{self.player.show_hand()}")

    def result(self):
        self.print_hands()
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

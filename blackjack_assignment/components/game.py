# Local Application Imports
from blackjack_assignment.components.dealer import Dealer
from blackjack_assignment.utils.input_prompt import prompt_for_input
from blackjack_assignment.utils.print_hands import print_hands
from blackjack_assignment.components.player import Player


class Game:
    def __init__(self):
        self.dealer = Dealer()  # Dealer needs to exist first
        self.player = Player([self.dealer.deal_card() for _ in range(2)])

    def __enter__(self):
        print("Dealing Hands...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Game Finished.")
        return

    def players_turn(self):
        while True:
            print_hands(self.dealer, self.player)
            decision = prompt_for_input("Hit or Stick?", ["Hit", "Stick"])
            if self.player.score > 21:
                self.player.bust()
                state = "Player is busted"
                break
            elif decision == 0:
                self.player.hit(self.dealer.deal_card())
            else:
                state = "Player is sticking"
                break
        print(state)
        return

    def dealers_turn(self):
        # Dealers turn
        # Early check to see if player is bust.
        if self.player.score > 21:
            return f"Dealer ({self.dealer.score}) wins. " \
                   f"Player ({self.player.score}) is bust."
        self.dealer.reveal_hidden()
        while not self.dealer.score > 17:
            print_hands(self.dealer, self.player)
            self.dealer.hit(self.dealer.deal_card())
        # Evaluate result once dealer hits stop condition
        if self.dealer.score > 21:
            outcome = f"Player ({self.player.score}) wins: " \
                      f"Dealer ({self.dealer.score}) is bust."
        elif self.dealer.score > self.player.score:
            outcome = f"Dealer ({self.dealer.score}) wins: " \
                      f"Player ({self.player.score}) < dealer"
        elif self.player.score > self.dealer.score:
            outcome = f"Player ({self.player.score}) wins: " \
                      f"player > dealer ({self.dealer.score})"
        else:  # self.dealer.score == self.player.score ## not good rewrite
            outcome = f"Draw game: Player ({self.player.score}) = " \
                      f"Dealer ({self.dealer.score})"
        print(outcome)
        return outcome

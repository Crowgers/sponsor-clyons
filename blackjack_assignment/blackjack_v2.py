#  Application Imports
from blackjack_assignment.components.dealer import Dealer
from blackjack_assignment.components.player import Player
from blackjack_assignment.utils.input_prompt import prompt_for_input


def player_turn(dealer: Dealer):
    while True:
        print(f"Player's hand: ({dealer.player.score}) "
              f"{dealer.player.show_hand()}")
        decision = prompt_for_input("Hit or Stick?", ["Hit", "Stick"])
        if dealer.player.score > 21:
            outcome = f"Dealer wins: player({dealer.player.score} is bust."
            break
        elif decision == 0:
            dealer.player.hit(dealer.deal_card())
        else:
            dealer.player.stick()
            outcome = ""
            break
    print(f"Player's {dealer.player.score} sticking hand: "
          f"{dealer.player.show_hand()}")
    return outcome


def dealer_turn(dealer: Dealer):
    # Dealers turn
    dealer.hit(first_hit=True)
    while not dealer.score > 17:
        dealer.hit()
        print(f"Dealers hand: {dealer.hand}"
              f"Dealer's score: {dealer.score}")
    # Results once hands are dealt
    if dealer.score > 21:
        outcome = f"Player({dealer.player.score}) wins: Dealer({dealer.score} is bust."
    elif dealer.score > dealer.player.score:
        outcome = f"Dealer wins: player({dealer.player.score}) < dealer" \
                  f"({dealer.score})"
    elif dealer.score == dealer.player.score:
        outcome = f"Draw game: player({dealer.player.score}) = dealer" \
                  f"({dealer.score})"
    else:
        outcome = f"Player wins: player({dealer.player.score}) > dealer" \
                  f"({dealer.score})"
    return outcome


def game():
    print("Initialising player and dealer...")
    dealer = Dealer()  # Initialises game
    outcome = player_turn(dealer)
    if not outcome:
        outcome = dealer_turn(dealer)
    return outcome


if __name__ == "__main__":
    play = 1
    while play:
        print(game())
        # Take user input and get the corresponding item from the list
        play = prompt_for_input("Would you like to play again?", ["No", "Yes"])

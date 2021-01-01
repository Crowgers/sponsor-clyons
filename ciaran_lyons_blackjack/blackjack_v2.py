#  Application Imports
from ciaran_lyons_blackjack.components.dealer import Dealer
from ciaran_lyons_blackjack.components.player import Player
from ciaran_lyons_blackjack.utils.input_prompt import prompt_for_input


def player_turn(dealer: Dealer, player: Player):
    while True:
        print(f"Player's ({player.score}) hand: {player.show_hand()}")
        decision = prompt_for_input("Hit or Stick?", ["Hit", "Stick"])
        if player.score > 21:
            outcome = f"Dealer wins: player({player.score} is bust."
            break
        elif decision == 0:
            player.hit(dealer.deal_card())
        else:
            player.stick()
            outcome = ""
            break
    print(f"Player's {player.score} sticking hand: {player.show_hand()}")
    return outcome


def dealer_turn(dealer: Dealer, player: Player):
    # Dealers turn
    dealer.hit(first_hit=True)
    while not dealer.score > 17:
        dealer.hit()
        print(f"Dealers hand: {dealer.hand}"
              f"Dealer's score: {dealer.score}")
    # Results once hands are dealt
    if dealer.score > 21:
        outcome = f"Player({player.score}) wins: Dealer({dealer.score} is bust."
    elif dealer.score > player.score:
        outcome = f"Dealer wins: player({player.score}) < dealer" \
                  f"({dealer.score})"
    elif dealer.score == player.score:
        outcome = f"Draw game: player({player.score}) = dealer({dealer.score})"
    else:
        outcome = f"Player wins: player({player.score}) > dealer" \
                  f"({dealer.score})"
    return outcome


def game():
    #  Initialise players (deck is a child of Dealer).
    print("Initialising player and dealer...")
    player = Player()
    dealer = Dealer()
    # Deal the player 2 cards
    print("Dealing players hand...")
    for i in range(2):
        player.hit(dealer.deal_card())
    # Deal dealer two cards one hidden
    print("Dealing dealers hand...")
    dealer.opening_deal()
    outcome = ""
    while not outcome:
        # Players turn
        print("Players turn...")
        outcome = player_turn(dealer, player)
        outcome = dealer_turn(dealer, player)
    return outcome


if __name__ == "__main__":
    play = 1
    while play:
        print(game())
        # Take user input and get the corresponding item from the list
        play = prompt_for_input("Would you like to play again?", ["No", "Yes"])

# Local Application Imports
from blackjack_assignment.components.game import Game
from blackjack_assignment.utils.input_prompt import prompt_for_input


def play_game():
    print("Welcome to blackjack!")
    play = 1
    with Game() as game:
        game.players_turn()
        game.dealers_turn()
    if not prompt_for_input(
        "Would you like to play again?",
        ["No", "Yes"]
    ):
        play_game()
    else:
        print("Exiting program.")


if __name__ == "__main__":
    play_game()

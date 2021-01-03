# Local Application Imports
from blackjack_assignment.components.game import Game
from blackjack_assignment.components.user_input import ask


if __name__ == "__main__":
    print("Welcome to blackjack!")
    finished = 0
    while not finished:
        Game().play()
        finished = ask(
            "Game Finished. Would you like to play again?",
            ["Yes", "No"]
        )
    print("Exiting program.")

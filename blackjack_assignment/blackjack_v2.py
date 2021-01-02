# Local Application Imports
from blackjack_assignment.components.game import Game
from blackjack_assignment.utils.user_input import ask


def start_game() -> Game:
    while True:
        yield Game()


if __name__ == "__main__":
    print("Welcome to blackjack!")
    play = 1
    while play:
        if new_game := next(start_game()):
            new_game.players_turn()
            new_game.dealers_turn()
            new_game.result()
            play = ask("Would you like to play again?", ["Yes", "No"])
        else:
            break
    print("Exiting program.")

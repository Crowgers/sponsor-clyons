from ciaran_lyons_blackjack.components.card import Card


class Player:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.sticking = False  # True means player is sticking

    def hit(self, card: Card):
        self.hand.append(card)
        self.score = sum([item.value for item in self.hand])
        return self.score

    def stick(self):
        self.sticking = True
        return self.sticking

    def show_hand(self):
        return [str(item) for item in self.hand]

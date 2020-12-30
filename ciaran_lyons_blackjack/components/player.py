class Player:
    def __init__(self):
        self.cards = []
        self.value_hand = sum([item.value for item in self.cards])
        self.state = "Play"  #  "play", or "stay"

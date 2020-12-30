class Dealer:
    def __init__(self):
        self.cards = []
        self.visible_card = ""
        self.value_hand = sum([item.value for item in self.cards])

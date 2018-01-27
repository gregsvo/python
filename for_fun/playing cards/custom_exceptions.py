class NotEnoughCards(Exception):
    def __init__(self):
        Exception.__init__(self, "There aren't enough cards in this pile.")

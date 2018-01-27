# Recently I was asked to model a library for a deck of cards.abs


class CardDeck(object):

    def __init__(self, suits=None, numbers=None, faces=None):
        self.suits = suits if suits else ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        self.numbers = numbers if numbers else [i for i in range(2, 11)]
        self.faces = faces if faces else ['Jack', 'Queen', 'King', 'Ace']
        self._cards = None
        self.discard_pile = None

    @property
    def cards(self):
        if self._cards:
            return self._cards
        self._cards = self._build_deck()
        return self.cards

    def _build_deck(self):
        cards = []
        for suit in self.suits:
            for number in self.numbers:
                card = (suit, number)
                cards.append(card)
            for face in self.faces:
                card = (suit, face)
                cards.append(card)
        return cards

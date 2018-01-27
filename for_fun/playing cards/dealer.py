from random import shuffle
from card_deck import CardDeck
from collections import defaultdict
from custom_exceptions import NotEnoughCards

DISCARD_PILE = 'discard_pile'
DRAW_PILE = 'draw_pile'


class Dealer(object):

    def __init__(self, deck=None, shuffling_requested=True):
        self._deck = deck if deck else CardDeck().cards
        self.discard_pile = []
        self.shuffling_requested = shuffling_requested
        self.draw_pile = self.shuffled_cards
        self.shown_cards = []

    @property
    def shuffled_cards(self):
        if self.shuffling_requested:
            shuffle(self._deck)
        return self._deck

    def _burn(self, num_of_cards_to_burn=1, show_burned_cards=False):
        burned_cards = self.draw_pile[:num_of_cards_to_burn]
        if show_burned_cards:
            print("I burned: {}".format(burned_cards))
        self.discard(burned_cards)
        self.draw_pile = self.draw_pile[num_of_cards_to_burn:]

    def deal(self, num_of_players, num_of_cards_to_each_player=None, deal_all_cards=False, leftovers_go_into=DRAW_PILE):
        if not deal_all_cards:
            if num_of_players * num_of_cards_to_each_player > len(self.draw_pile):
                raise NotEnoughCards()
        dealings = defaultdict(list)
        while len(self.draw_pile) > num_of_players:
            for round in range(0, num_of_cards_to_each_player):
                for player in range(1, num_of_players + 1):
                    dealings[player].extend(self.hit_me())
            if leftovers_go_into == DISCARD_PILE:
                self.discard_pile.extend(self.draw_pile)
                self.draw_pile = []
            return dealings

    def flop(self):
        self.shown_cards.extend(self.hit_me(burn_first=True, requested=3))
        print("Burning one card...")
        print(self.shown_cards)

    def turn(self):
        self.shown_cards.extend(self.hit_me(burn_first=True, requested=1))
        print("Burning one card...")
        print(self.shown_cards)

    def hit_me(self, burn_first=False, requested=1):
        if burn_first:
            self._burn()
        outgoing_cards = self.draw_pile[:requested]
        self.draw_pile = self.draw_pile[requested:]
        return outgoing_cards

    def discard(self, cards):
        self.discard_pile.extend(cards)

    def show_cards_in_discard_pile(self):
        print(self.discard_pile)

    def show_cards_in_deck(self):
        print(self.draw_pile)

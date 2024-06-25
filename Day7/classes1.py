from enum import Enum
from collections import Counter

order = '23456789TJQKA'


class HandType(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

    def __gt__(self, other):
        return self.value > other.value


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.type = self.compute_type()
        self.rank = None

    def compute_type(self):
        count = Counter(self.cards)
        if len(count) == 1:
            return HandType.FIVE_OF_A_KIND
        elif len(count) == 2:
            if 4 in count.values():
                return HandType.FOUR_OF_A_KIND
            return HandType.FULL_HOUSE
        elif len(count) == 3:
            if 3 in count.values():
                return HandType.THREE_OF_A_KIND
            return HandType.TWO_PAIR
        elif len(count) == 4:
            return HandType.PAIR
        else:
            return HandType.HIGH_CARD

    def compare_cards(self, other):
        for card in zip(self.cards, other.cards):
            if card[0] != card[1]:
                return order.index(card[0]) > order.index(card[1])

    def get_winnings(self):
        if self.rank is not None:
            return self.bid * self.rank

    def __eq__(self, other):
        return self.cards == other.cards

    def __gt__(self, other):
        if self.type == other.type:
            return self.compare_cards(other)
        else:
            return self.type > other.type

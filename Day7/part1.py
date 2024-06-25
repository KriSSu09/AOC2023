from Day7.classes1 import Hand

with open('input.txt') as f:
    hands = sorted(list(map(lambda x: Hand(*x.split()), f.readlines())))
    for idx, hand in enumerate(hands):
        hand.rank = idx + 1
    print(sum(map(lambda x: x.get_winnings(), hands)))

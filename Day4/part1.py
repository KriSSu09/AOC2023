with open('input.txt') as f:
    cards = {idx + 1: sets.split(' | ') for idx, sets in enumerate([line.split(': ')[1] for line in f.readlines()])}
    for card_idx in cards:
        cards[card_idx] = [set([int(num) for num in sets.split()]) for sets in cards[card_idx]]
    print(sum(2 ** (len(cards[card_idx][0].intersection(cards[card_idx][1])) - 1) for card_idx in cards if len(cards[card_idx][0].intersection(cards[card_idx][1])) != 0))

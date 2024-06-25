with open('input.txt') as f:
    cards = {idx + 1: sets.split(' | ') for idx, sets in enumerate([line.split(': ')[1] for line in f.readlines()])}
    for card_idx in cards:
        cards[card_idx] = [set([int(num) for num in sets.split()]) for sets in cards[card_idx]]
        cards[card_idx].append(1)
    for card_idx in cards:
        for card in range(cards[card_idx][2]):
            for i in range(len(cards[card_idx][0].intersection(cards[card_idx][1]))):
                cards[card_idx + i + 1][2] += 1
    print(sum(cards[card_idx][2] for card_idx in cards))

with open('input.txt') as f:
    games = {idx + 1: sets.split(';') for idx, sets in enumerate([line.split(': ')[1] for line in f.readlines()])}
    limits = {'red': 12, 'green': 13, 'blue': 14}
    answer = 0
    for idx in games:
        possible = True
        for shown in games[idx]:
            numbers = {'red': 0, 'green': 0, 'blue': 0}
            for cubes in shown.split(','):
                nr, color = cubes.split()
                numbers[color] = int(nr)
            if numbers['red'] > limits['red'] or numbers['green'] > limits['green'] or numbers['blue'] > limits['blue']:
                possible = False
                break
        if possible:
            answer += idx
    print(answer)

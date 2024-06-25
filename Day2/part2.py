import math

with open('input.txt') as f:
    games = [sets.split(';') for idx, sets in enumerate([line.split(': ')[1] for line in f.readlines()])]
    answer = 0
    for game in games:
        numbers = {'red': [], 'green': [], 'blue': []}
        for shown in game:
            for cubes in shown.split(','):
                nr, color = cubes.split()
                numbers[color].append(int(nr))
        answer += math.prod([max(numbers[color]) for color in numbers])
    print(answer)

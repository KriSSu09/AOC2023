with open('input.txt') as f:
    digits = list(map(lambda x: [c for c in x if c.isdigit()], f.readlines()))
    print(sum([int("".join([line[0], line[-1]])) for line in digits]))

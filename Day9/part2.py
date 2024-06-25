with open('input.txt') as f:
    answer = 0
    for line in f.readlines():
        values = [list(map(lambda x: int(x), line.strip().split()))]
        while sum(values[-1]):
            new_values = []
            for i in range(len(values[-1]) - 1, 0, -1):
                new_values.append(values[-1][i] - values[-1][i - 1])
            values.append(list(reversed(new_values)))
        values[-1].insert(0, 0)
        for idx, value in enumerate(list(reversed(values))[1:]):
            value.insert(0, value[0] - values[-idx - 1][0])
        answer += values[0][0]
    print(answer)

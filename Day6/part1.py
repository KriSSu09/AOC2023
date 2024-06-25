with open('input.txt') as f:
    times = list(map(lambda x: int(x), f.readline().strip().split(':')[1].strip().split()))
    distances = list(map(lambda x: int(x), f.readline().strip().split(':')[1].strip().split()))
    answer = 1
    for idx, time in enumerate(times):
        v = 1
        ways = 0
        while v <= time // 2:
            if v * (time - v) > distances[idx]:
                ways += 1
            v += 1
        answer *= (ways * 2 - (0 if time % 2 else 1))
    print(answer)

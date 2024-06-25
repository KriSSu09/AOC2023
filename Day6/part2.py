with open('input.txt') as f:
    time = int("".join(f.readline().strip().split(':')[1].strip().split()))
    distance = int("".join(f.readline().strip().split(':')[1].strip().split()))
    answer = 0
    v = 1
    while v <= time // 2:
        if v * (time - v) > distance:
            answer += 1
        v += 1
    answer = (answer * 2 - (0 if time % 2 else 1))
    print(answer)

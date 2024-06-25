with open('input.txt') as f:
    lines = ['.' + line.replace('\n', '.') for line in f.readlines()]
    lines.append('.' * len(lines[0]))
    lines.insert(0, '.' * len(lines[0]))
    dx = [1, 0, 1, -1, 0, -1, 1, -1]
    dy = [0, 1, 1, 0, -1, -1, -1, 1]
    answer = 0
    for i, line in enumerate(lines[1:len(lines)]):
        nr = []
        isPart = False
        for j, char in enumerate(line[1:len(line)]):
            if char.isdigit():
                nr.append(char)
                if not isPart:
                    for k in range(len(dx)):
                        if lines[i + 1 + dx[k]][j + 1 + dy[k]] == '.' or lines[i + 1 + dx[k]][j + 1 + dy[k]].isdigit():
                            continue
                        isPart = True
                        break
            else:
                if isPart:
                    answer += int(''.join(nr))
                nr = []
                isPart = False
        if isPart:
            answer += int(''.join(nr))
        nr = []
        isPart = False
    if isPart:
        answer += int(''.join(nr))
    print(answer)

with open('input.txt') as f:
    lines = ['.' + line.replace('\n', '.') for line in f.readlines()]
    lines.append('.' * len(lines[0]))
    lines.insert(0, '.' * len(lines[0]))
    dx = [1, 0, 1, -1, 0, -1, 1, -1]
    dy = [0, 1, 1, 0, -1, -1, -1, 1]
    answer = 0
    for i, line in enumerate(lines[1:len(lines)]):
        for j, char in enumerate(line[1:len(line)]):
            if char == '*':
                nrs = set()
                for k in range(len(dx)):
                    x = i + 1 + dx[k]
                    y = j + 1 + dy[k]
                    if lines[x][y].isdigit():
                        nr = lines[x][y]
                        y2 = y + 1
                        while lines[x][y2].isdigit() and y2 < len(lines[x]) - 1:
                            nr += lines[x][y2]
                            y2 += 1
                        y2 = y - 1
                        while lines[x][y2].isdigit() and y2 > 0:
                            nr = lines[x][y2] + nr
                            y2 -= 1
                        nrs.add(nr)
                if len(nrs) == 2:
                    answer += int(nrs.pop()) * int(nrs.pop())
    print(answer)

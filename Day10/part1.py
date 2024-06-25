with open('input.txt') as f:
    pipe_directions = {'|': {(1, 0), (-1, 0)}, '-': {(0, 1), (0, -1)}, 'L': {(-1, 0), (0, 1)}, 'J': {(-1, 0), (0, -1)},
                       '7': {(1, 0), (0, -1)}, 'F': {(1, 0), (0, 1)}, 'S': {(1, 0), (0, 1), (0, -1), (-1, 0)}}
    matrix = [line.strip() for line in f.readlines()]
    for i in range(len(matrix)):
        if 'S' in matrix[i]:
            start = (i, matrix[i].index('S'))
            break
    loops = []
    S_directions = set()
    for x, y in pipe_directions['S']:
        if 0 <= start[0] + x < len(matrix) and 0 <= start[1] + y < len(matrix[0]) and matrix[start[0] + x][
         start[1] + y] != '.':
            neighbor = matrix[start[0] + x][start[1] + y]
            for dx, dy in pipe_directions[neighbor]:
                if 0 <= start[0] + x + dx < len(matrix) and 0 <= start[1] + y + dy < len(matrix[0]) and matrix[
                 start[0] + x + dx][start[1] + y + dy] == 'S':
                    S_directions.add((x, y))
    pipe_directions['S'] = S_directions
    discovery_matrix = [['.' for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    discovery_matrix[start[0]][start[1]] = 'S'
    stack = [start]
    while len(stack):
        x, y = stack.pop()
        discovery_matrix[x][y] = matrix[x][y]
        debug = matrix[x][y]
        for dx, dy in pipe_directions[matrix[x][y]]:
            if 0 <= x + dx < len(matrix) and 0 <= y + dy < len(matrix[0]) and discovery_matrix[x + dx][
             y + dy] == '.' and matrix[x + dx][y + dy] != '.':
                stack.append((x + dx, y + dy))
    queue = [start]
    distance_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    while len(queue):
        x, y = queue.pop(0)
        for dx, dy in pipe_directions[matrix[x][y]]:
            if 0 <= x + dx < len(matrix) and 0 <= y + dy < len(matrix[0]) and distance_matrix[x + dx][
             y + dy] == 0 and matrix[x + dx][y + dy] != '.':
                distance_matrix[x + dx][y + dy] = distance_matrix[x][y] + 1
                queue.append((x + dx, y + dy))
    print(max([max(row) for row in distance_matrix]))
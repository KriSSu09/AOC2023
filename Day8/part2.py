with open('input.txt') as f:
    directions = list(map(lambda x: 0 if x == 'L' else 1, list(f.readline().strip())))
    nodes = {line[0].strip(): tuple(line[1].strip().replace('(', '').replace(')', '').split(', ')) for line in
             map(lambda x: x.split(' = '), f.readlines()[1:])}
    current_nodes = list(filter(lambda x: x[-1] == 'A', nodes.keys()))
    current_direction = 0
    steps = 0
    while len(list(filter(lambda x: x[-1] != 'Z', current_nodes))):
        current_nodes = list(map(lambda x: nodes[x][directions[current_direction]], current_nodes))
        current_direction = (current_direction + 1) % len(directions)
        steps += 1
    print(steps)

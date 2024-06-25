import threading
from math import lcm


def task(idx, node, direction, local_steps):
    global nodes, directions, thread_steps
    node = nodes[node][directions[direction]]
    direction = (direction + 1) % len(directions)
    local_steps += 1
    while node[-1] != 'Z':
        node = nodes[node][directions[direction]]
        direction = (direction + 1) % len(directions)
        local_steps += 1
    thread_steps[idx].append((local_steps, node, direction))


with open('input.txt') as f:
    directions = list(map(lambda x: 0 if x == 'L' else 1, list(f.readline().strip())))
    nodes = {line[0].strip(): tuple(line[1].strip().replace('(', '').replace(')', '').split(', ')) for line in
             map(lambda x: x.split(' = '), f.readlines()[1:])}
    current_nodes = list(filter(lambda x: x[-1] == 'A', nodes.keys()))
    thread_steps = [[(0, node, 0)] for idx, node in enumerate(current_nodes)]
    threads = [threading.Thread(target=task, args=(idx, thread_step[-1][1], thread_step[-1][2], thread_step[-1][0]))
               for idx, thread_step in enumerate(thread_steps)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    cycles = []
    for thread_step in thread_steps:
        cycles.append(thread_step[-1][0])
    print(lcm(*cycles))

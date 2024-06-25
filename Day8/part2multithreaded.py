import threading


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
    current_min = 1
    while True:
        print(current_min)
        threads = [threading.Thread(target=task, args=(idx, thread_step[-1][1], thread_step[-1][2], thread_step[-1][0]))
                   for idx, thread_step in enumerate(thread_steps)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        done2 = False
        while True:
            thread_steps = [list(filter(lambda x: x[0] > current_min, thread_step)) for thread_step in thread_steps]
            current_min = min([min(map(lambda x: x[0], thread_step)) for thread_step in thread_steps])
            done3 = False
            for thread_step in thread_steps:
                if len(thread_step) == 1 and thread_step[0][0] == current_min:
                    done3 = True
                    break
            if done3:
                current_min -= 1
                break
            done = [current_min in map(lambda x: x[0], thread_step) for thread_step in thread_steps]
            if all(done):
                print(current_min)
                done2 = True
                break
            for thread_step in thread_steps:
                if len(thread_step) > 1:
                    break
            else:
                break
        if done2:
            break

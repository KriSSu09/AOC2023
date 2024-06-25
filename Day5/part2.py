from Day5.classes import Almanac

with open('input.txt') as f:
    seed_ranges = list(map(lambda x: int(x), f.readline().strip().split(': ')[1].split()))
    seeds = set()
    for seed_range_start, seed_range_length in zip(seed_ranges[::2], seed_ranges[1::2]):
        seeds.add(range(seed_range_start, seed_range_start + seed_range_length))
    almanac = Almanac()
    mappings = f.read().strip().split('\n\n')
    for m in mappings:
        source_target, ranges = m.split(':\n')
        source, target = source_target.replace('to-', '').replace(' map', '').split('-')
        almanac.add_map(source, target)
        for r in ranges.split('\n'):
            almanac.get_map(source, target).add_range(*map(lambda x: int(x), r.split()))
    curr_min = 1
    found = False
    while not found:
        if curr_min % 100000 == 0:
            print(curr_min)
        seed_value = almanac.get_location_to_seed_value(curr_min)
        for seed_range in seeds:
            if almanac.get_location_to_seed_value(curr_min) in seed_range:
                found = True
                break
        if not found:
            curr_min += 1
    print('Found: ', curr_min)

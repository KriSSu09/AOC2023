from Day5.classes import Almanac

with open('input.txt') as f:
    seeds = list(map(lambda x: int(x), f.readline().strip().split(': ')[1].split()))
    almanac = Almanac()
    mappings = f.read().strip().split('\n\n')
    for m in mappings:
        source_target, ranges = m.split(':\n')
        source, target = source_target.replace('to-', '').replace(' map', '').split('-')
        almanac.add_map(source, target)
        for r in ranges.split('\n'):
            almanac.get_map(source, target).add_range(*map(lambda x: int(x), r.split()))
    current_map = almanac.get_map_by_source('seed')
    while current_map.target != 'location':
        seeds = list(map(lambda x: current_map.get_mapping(x), seeds))
        current_map = almanac.get_map_by_source(current_map.target)
    seeds = list(map(lambda x: current_map.get_mapping(x), seeds))
    print(min(seeds))

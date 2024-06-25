class AlmanacMap:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.map = []

    def add_range(self, destination_range_start, source_range_start, range_length):
        self.map.append((range(destination_range_start, destination_range_start + range_length),
                         range(source_range_start, source_range_start + range_length)))

    def get_mapping(self, value):
        for destination_range, source_range in self.map:
            if value in source_range:
                return destination_range[source_range.index(value)]
        return value

    def get_reverse_mapping(self, value):
        for destination_range, source_range in self.map:
            if value in destination_range:
                return source_range[destination_range.index(value)]
        return value


class Almanac:
    def __init__(self):
        self.maps = []

    def add_map(self, source, target):
        self.maps.append(AlmanacMap(source, target))

    def get_map(self, source, target):
        return next(filter(lambda m: m.source == source and m.target == target, self.maps))

    def get_map_by_source(self, source):
        return next(filter(lambda m: m.source == source, self.maps))

    def get_map_by_target(self, target):
        return next(filter(lambda m: m.target == target, self.maps))

    def get_location_to_seed_value(self, value):
        current_map = self.get_map_by_target('location')
        while current_map.source != 'seed':
            value = current_map.get_reverse_mapping(value)
            current_map = self.get_map_by_target(current_map.source)
        return current_map.get_reverse_mapping(value)


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

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

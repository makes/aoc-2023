from string import ascii_letters, punctuation


class Range:
    def __init__(self, dest_start, src_start, length):
        self._dest_start = dest_start
        self._src_start = src_start
        self._len = length

    @property
    def start(self):
        return self._src_start

    @property
    def stop(self):
        return self._src_start + self._len - 1

    @property
    def length(self):
        return self._len

    def has(self, src):
        return src >= self._src_start and src < self._src_start + self._len

    def is_endpoint(self, src):
        return src == self.start or src == self.stop

    def split_at(self, length):
        assert length < self._len
        r1 = Range(self._dest_start, self._src_start, length)
        r2 = Range(
            length + self._dest_start, length + self._src_start, self._len - length
        )
        return r1, r2

    def convert_scalar(self, src):
        if not self.has(src):
            raise ValueError("Cannot convert off-range value.")
        return (src - self._src_start) + self._dest_start


class Map:
    def __init__(self, lines):
        self._ranges = []
        for ln in lines:
            dest, src, length = [int(x) for x in ln.split()]
            self._ranges.append(Range(dest, src, length))

    @property
    def start_points(self):
        return [r.start for r in self._ranges]

    @property
    def stop_points(self):
        return [r.stop for r in self._ranges]

    def convert_scalar(self, src):
        for r in self._ranges:
            if r.has(src):
                return r.convert_scalar(src)
        return src

    def convert_ranges(self, ranges):
        for start in self.start_points:
            out = []
            for r in ranges:
                if r.has(start) and not r.is_endpoint(start):
                    out += r.split_at(start - r.start)
                else:
                    out += [r]
            ranges = out
        for stop in self.stop_points:
            out = []
            for r in ranges:
                if r.has(stop) and not r.is_endpoint(stop):
                    out += r.split_at(stop - r.start + 1)
                else:
                    out += [r]
            ranges = out
        ranges = [
            Range(self.convert_scalar(x.start), self.convert_scalar(x.start), x.length)
            for x in ranges
        ]
        return ranges


class MapChain:
    def __init__(self):
        self._maps = []

    def append(self, map):
        self._maps.append(map)

    def convert_scalar(self, src):
        val = src
        for m in self._maps:
            val = m.convert(val)
        return val

    def convert_ranges(self, ranges):
        for m in self._maps:
            ranges = m.convert_ranges(ranges)
        return ranges


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        input_str = f.read()

    blocks = input_str.split("\n\n")
    blocks = [filter(lambda x: x not in ascii_letters + punctuation, s) for s in blocks]
    blocks = ["".join(list(x)).strip() for x in blocks]

    seed_ints = [int(x) for x in blocks[0].split()]
    seed_tups = [(seed_ints[i], seed_ints[i + 1]) for i in range(0, len(seed_ints), 2)]
    seed_ranges = [Range(x[0], x[0], x[1]) for x in seed_tups]

    maps = MapChain()
    for b in blocks[1:]:
        maps.append(Map(b.split("\n")))
    location_ranges = maps.convert_ranges(seed_ranges)

    print(min([x.start for x in location_ranges]))

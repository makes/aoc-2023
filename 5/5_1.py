from string import ascii_letters, punctuation

class MapRange:
    def __init__(self, dest_start, src_start, length):
        self._dest_start = dest_start
        self._src_start = src_start
        self._len = length

    def in_range(self, src):
        return src >= self._src_start and src < self._src_start + self._len

    def convert(self, src):
        if not self.in_range(src):
            raise ValueError("Cannot convert off-range value.")
        return (src - self._src_start) + self._dest_start

class Map:
    def __init__(self, lines):
        self._ranges = []
        for ln in lines:
            dest, src, length = [int(x) for x in ln.split()]
            self._ranges.append(MapRange(dest, src, length))

    def convert(self, src):
        for r in self._ranges:
            if r.in_range(src):
                return r.convert(src)
        return src

class MapChain:
    def __init__(self):
        self._maps = []

    def append(self, map):
        self._maps.append(map)

    def convert(self, src):
        val = src
        for m in self._maps:
            val = m.convert(val)
        return val

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        input_str = f.read()

    blocks = input_str.split('\n\n')
    blocks = [filter(lambda x: x not in ascii_letters + punctuation, s) for s in blocks]
    blocks = [''.join(list(x)).strip() for x in blocks]

    seeds = [int(x) for x in blocks[0].split()]

    maps = MapChain()
    for b in blocks[1:]:
        maps.append(Map(b.split('\n')))
    locations = map(maps.convert, seeds)

    print(min(locations))


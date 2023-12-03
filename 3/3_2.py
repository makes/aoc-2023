from string import digits
from math import prod

lookaround_vec = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def is_symbol(c):
    return c != "." and c not in digits


class Number:
    def __init__(self, start, value):
        self._length = len(str(value))
        self._start = start
        self.value = value

    @property
    def points(self):
        x0, y0 = self._start
        return [(x + x0, y0) for x in range(self._length)]

    def has_adjacent_symbol(self, grid):
        pts = self.points
        for p in pts:
            if grid.point_has_adjacent_symbol(p):
                return True
        return False

    def is_adjacent(self, point):
        x0, y0 = point
        for v in lookaround_vec:
            x, y = v
            if (x + x0, y + y0) in self.points:
                return True
        return False


class Grid:
    def __init__(self, lines):
        lines = [l.strip() for l in lines]
        self.width = len(lines[0]) + 2
        self.height = len(lines) + 2
        self._grid = ["."] * self.width * self.height
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                self._grid[x + 1 + (y + 1) * self.width] = c
        self._numbers = self._find_numbers()

    def char_at(self, coords):
        x, y = coords
        return self._grid[x + y * self.width]

    def __getitem__(self, index):
        x = index % self.width
        y = index // self.width
        return x, y, self.char_at((x, y))

    def point_has_adjacent_symbol(self, point):
        for v in lookaround_vec:
            if is_symbol(self.char_at((point[0] + v[0], point[1] + v[1]))):
                return True
        return False

    def _find_numbers(self):
        numbers = []
        for y in range(self.height):
            x = 0
            while x < self.width:
                if self.char_at((x, y)) in digits:
                    start = (x, y)
                    d = ""
                    while self.char_at((x, y)) in digits:
                        d += self.char_at((x, y))
                        x += 1
                    numbers.append(Number(start, int(d)))
                    x -= 1
                x += 1
        return numbers

    @property
    def numbers(self):
        return tuple(self._numbers)

    def get_adjacent_numbers(self, point):
        nums = []
        for n in self._numbers:
            if n.is_adjacent(point):
                nums.append(n)
        return nums


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    grid = Grid(lines)
    sum = 0
    for x, y, item in grid:
        if item == "*":
            adjacent_nums = grid.get_adjacent_numbers((x, y))
            if len(adjacent_nums) < 2:
                continue
            vals = [n.value for n in adjacent_nums]
            sum += prod(vals)
    print(sum)

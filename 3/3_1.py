from string import digits


def is_symbol(c):
    return c != "." and c not in digits


class Number:
    def __init__(self, start, value):
        self._length = len(str(value))
        self._start = start
        self.value = value

    def get_points(self):
        x0, y0 = self._start
        return [(x + x0, y0) for x in range(self._length)]

    def has_adjacent_symbol(self, grid):
        pts = self.get_points()
        for p in pts:
            if grid.point_has_adjacent_symbol(p):
                return True
        return False


class Grid:
    def __init__(self, lines):
        lines = [l.strip() for l in lines]
        self._width = len(lines[0]) + 2
        self._height = len(lines) + 2
        self._grid = ["."] * self._width * self._height
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                self._grid[x + 1 + (y + 1) * self._width] = c

    def char_at(self, coords):
        x, y = coords
        return self._grid[x + y * self._width]

    def point_has_adjacent_symbol(self, point):
        vec = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for v in vec:
            if is_symbol(self.char_at((point[0] + v[0], point[1] + v[1]))):
                return True
        return False

    def get_numbers(self):
        numbers = []
        for y in range(self._height):
            x = 0
            while x < self._width:
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


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    grid = Grid(lines)
    numbers = grid.get_numbers()
    sum = 0
    for n in numbers:
        if n.has_adjacent_symbol(grid):
            sum += n.value
    print(sum)

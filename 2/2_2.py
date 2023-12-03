from functools import reduce

class CubeSet:
    def __init__(self, d):
        self._colors = d

    @classmethod
    def from_vals(cls, r, g, b):
        return cls({'red': r, 'green': g, 'blue': b})

    @classmethod
    def from_string(cls, s):
        colors = {'red': 0, 'green': 0, 'blue': 0}
        cols = s.split(',')
        for c in cols:
            c = c.strip().split(' ')
            n = int(c[0])
            i = c[1]
            colors[i] = n
        return cls(colors)

    def __getitem__(self, index):
        return self._colors[index]

    def power(self):
        return reduce(lambda x, y: x * y, self._colors.values())

    def is_subset_of(self, cubeset):
        ret = True
        for c in self._colors:
            ret = ret & (self[c] <= cubeset[c])
        return ret

class CubeGame:
    def __init__(self, s):
        s = s.split(':')
        self.game_id = int(s[0].split(' ')[1])
        samples = s[1].split(';')
        self._samples = []
        for sample_str in samples:
            self._samples.append(CubeSet.from_string(sample_str))

    def __getitem__(self, index):
        return self._samples[index]

    def minimum_set(self):
        r = max(s['red'] for s in self._samples)
        g = max(s['green'] for s in self._samples)
        b = max(s['blue'] for s in self._samples)
        return CubeSet.from_vals(r, g, b)

    def is_possible_given_population(self, pop):
        return self.minimum_set().is_subset_of(pop)

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    games = {}
    for l in lines:
        game = CubeGame(l)
        if game.game_id in games:
            raise ValueError("Duplicate game_id={game.game_id}.")
        games[game.game_id] = game

    power_sum = 0
    for game_id, game in games.items():
        power_sum += game.minimum_set().power()
    print(power_sum)


class CubeSet:
    def __init__(self, d):
        self._colors = d

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

    def is_possible_given_population(self, pop):
        for sample in self._samples:
            if not sample.is_subset_of(pop):
                return False
        return True


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    games = {}
    for l in lines:
        game = CubeGame(l)
        if game.game_id in games:
            raise ValueError("Duplicate game_id={game.game_id}.")
        games[game.game_id] = game

    pop = CubeSet({'red': 12, 'green': 13, 'blue': 14})

    id_sum = 0
    for game_id, game in games.items():
        id_sum += game_id * game.is_possible_given_population(pop)
    print(id_sum)


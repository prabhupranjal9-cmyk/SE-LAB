import random


class AI:
    def __init__(self, size=6):
        self.size = size
        self.tried = set()
        self.hits = set()

    def choose(self):
        if len(self.tried) >= self.size * self.size:
            return None

        adjacent = []

        for r, c in self.hits:
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < self.size
                    and 0 <= nc < self.size
                    and (nr, nc) not in self.tried
                ):
                    adjacent.append((nr, nc))

        if adjacent:
            pos = random.choice(adjacent)
        else:
            options = [
                (r, c)
                for r in range(self.size)
                for c in range(self.size)
                if (r, c) not in self.tried
            ]
            pos = random.choice(options)

        self.tried.add(pos)
        return pos

    def record_hit(self, pos):
        self.hits.add(pos)
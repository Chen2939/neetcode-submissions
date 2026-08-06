class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        x, y = point
        self.ptsCount[(x, y)] += 1
        self.pts.append((x, y))

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.pts:
            if abs(y-py) != abs(x-px) or x == px or y == py: continue

            res += (self.ptsCount[(x, py)] * self.ptsCount[(px, y)])
        
        return res


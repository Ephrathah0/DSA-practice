class DetectSquares:

    def __init__(self):
        self.pointsHash = defaultdict(dict)

    def add(self, point: List[int]) -> None:
        self.pointsHash[point[0]][point[1]] = self.pointsHash[point[0]].get(point[1], 0) + 1

    def count(self, point: List[int]) -> int:
        count, x1, y1 = 0, point[0], point[1]
        for y2 in self.pointsHash[x1]:
            if y2 == y1:
                continue
            diff = abs(y2 - y1)
            leftX, rightX = x1 - diff, x1 + diff
            count += self.pointsHash[leftX].get(y1, 0) * self.pointsHash[leftX].get(y2, 0) * self.pointsHash[x1].get(y2, 0)
            count += self.pointsHash[rightX].get(y1, 0) * self.pointsHash[rightX].get(y2, 0) * self.pointsHash[x1].get(y2, 0)
        return count

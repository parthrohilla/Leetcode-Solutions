class DetectSquares:

    def __init__(self):
        self.points_map = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        key = tuple(point)
        self.points_map[key] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        ans = 0
        a, b = point
        for p in self.points:
            x, y = p
            if (abs(b-y) == abs(a-x)) and a!=x and y != b:
                ans += self.points_map[tuple([x, b])] * self.points_map[tuple([a, y])]
                
        return ans
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
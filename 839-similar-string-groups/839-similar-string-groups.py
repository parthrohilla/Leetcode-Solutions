class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        groups = n
        self.parent = [i for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if self.similar(strs[i], strs[j]) and self.union(i, j):
                    groups -= 1
        return groups

    def similar(self, a, b):
        diff = 0
        for char1, char2 in zip(a, b):
            if char1 != char2:
                diff += 1
            if diff > 2:
                return False
        return True

    def find(self, x):
        if self.parent[x] == x: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, s1, s2):
        p1, p2 = self.find(s1), self.find(s2)
        if p1 == p2:
            return False
        else:
            self.parent[p2] = p1
            return True
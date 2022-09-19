class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for i,p in enumerate(parent):
            tree[p].append(i)
        
        self.ans = 1
        def dfs(node):
            temp = []
            for child in tree[node]:
                small = dfs(child)
                if s[node] != s[child]: 
                    temp.append(small)
                temp.sort()
                if len(temp) >= 2: 
                    self.ans = max(self.ans, 1 + temp[-1] + temp[-2])
                elif temp: 
                    self.ans = max(self.ans, 1 + temp[-1])
            
            return 1 if len(temp) == 0 else 1 + temp[-1]
        
        dfs(0)
        return self.ans
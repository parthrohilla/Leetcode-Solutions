class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        # Create adjacency list of the form {parent : [child1, child2 ... childn]}
        for i,p in enumerate(parent):
            tree[p].append(i)
        # the most trivial case, ans would be 1 if either 1 node tree or if all nodes have the same characters
        self.ans = 1
        # dfs() here returns the longest path starting from the current node
        # So for each node we calcuate the longest path from it's child sub-tree and combine results
        def dfs(node):
            temp = []
            for child in tree[node]:
                small = dfs(child)
                if s[node] != s[child]: 
                    temp.append(small)
                temp.sort()
                if len(temp) >= 2: self.ans = max(self.ans, 1 + temp[-1] + temp[-2])
                elif temp: self.ans = max(self.ans, 1 + temp[-1])
            return 1 if len(temp) == 0 else 1 + temp[-1]
        # Calling dfs() from root of the tree
        dfs(0)
        return self.ans
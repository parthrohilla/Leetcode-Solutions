class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        G = defaultdict(list)
        for i,p in enumerate(parents):
            if p != -1:
                G[i].append(p)
                G[p].append(i)
        
        @lru_cache(None)
        def dfs(i,p):
            S = 1
            for nei in G[i]:
                if nei != p:
                    S += dfs(nei,i)
            return S
        
        N = len(parents)
        seen = defaultdict(int)
        for i in range(N):
            score = 1
            for nei in G[i]:
                score *= dfs(nei,i)
            seen[score] += 1

        return seen[max(seen.keys())]
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        indegrees = defaultdict(int)
        
        for i in range(len(recipes)):
            for ingr in ingredients[i]:
                adj[ingr].append(recipes[i])
                indegrees[recipes[i]] += 1
        
        ans = []
        q = deque()
        for supply in supplies:
            q.append(supply)
        
        while q:
            sup = q.popleft()
            for k in adj[sup]:
                indegrees[k] -= 1
                if indegrees[k] == 0: 
                    q.append(k)
                    ans.append(k)
        return ans
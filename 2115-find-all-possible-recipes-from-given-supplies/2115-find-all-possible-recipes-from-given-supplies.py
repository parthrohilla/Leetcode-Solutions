class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        indegrees = defaultdict(int)
        # Make a Graph such that all ingredients lead us to the recipe
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                adj[ingredient].append(recipes[i])
                indegrees[recipes[i]] += 1
        # Add supplies to the queue, as we would use the supplies and remove all the things we can make with that ingredient
        ans, q = [], deque()
        for supply in supplies:
            q.append(supply)
        
        while q:
            ingredient = q.popleft()
            for product in adj[ingredient]:
                indegrees[product] -= 1
                if indegrees[product] == 0: 
                    q.append(product)
                    ans.append(product)
        return ans
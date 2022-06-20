class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def dfs(index, subset, total):
            if total == target:
                output.append(subset)
                return
            
            if index >= len(candidates) or total > target:
                return 
            
            dfs(index, subset+[candidates[index]], total+candidates[index])
            dfs(index+1, subset, total)
        
        dfs(0,[],0)
        return output
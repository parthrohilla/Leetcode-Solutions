# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        seen = defaultdict(int)
        
        def dfs(node):
            if not node: return 0
            S = dfs(node.left) + node.val + dfs(node.right)
            seen[S] += 1
            return S
        
        dfs(root)
        A = defaultdict(list)
        for K,V in seen.items():
            A[V].append(K)
            
        return A[max(A.keys())]
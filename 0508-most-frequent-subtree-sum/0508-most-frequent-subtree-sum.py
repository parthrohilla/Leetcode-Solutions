# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        seen = []
        
        def dfs(node):
            if not node: return 0
            S = dfs(node.left) + node.val + dfs(node.right)
            seen.append(S)
            return S
        
        dfs(root)
        temp = defaultdict(list)
        C = Counter(seen)
        for K,V in C.items():
            temp[V].append(K)
            
        return temp[max(temp.keys())]
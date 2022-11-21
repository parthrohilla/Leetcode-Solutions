# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        G = defaultdict(list)
        
        def build(node):
            if not node: return
            
            if node.left:
                G[node.val].append(node.left.val)
                G[node.left.val].append(node.val)
                build(node.left)
                
            if node.right:
                G[node.val].append(node.right.val)
                G[node.right.val].append(node.val)
                build(node.right)

        build(root)
        
        Q = deque()
        Q.append(start)
        infected = {start}
        time = 0
        
        while Q:
            K = len(Q)
            for _ in range(K):
                node = Q.popleft()
                for nei in G[node]:
                    if nei not in infected:
                        Q.append(nei)
                        infected.add(nei)
            time += 1
        
        return time - 1
                
                

        
            
            
            
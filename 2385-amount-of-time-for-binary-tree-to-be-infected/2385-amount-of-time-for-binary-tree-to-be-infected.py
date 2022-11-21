# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Build Graph 
        def build_graph(node):
            if not node: return
            
            if node.left:
                G[node.val].append(node.left.val)
                G[node.left.val].append(node.val)
                build_graph(node.left)
                
            if node.right:
                G[node.val].append(node.right.val)
                G[node.right.val].append(node.val)
                build_graph(node.right)
        
        G = defaultdict(list)
        build_graph(root)
        
        # BFS Implementation
        Q = deque([start])
        infected, time = {start}, 0
        
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
                
                

        
            
            
            
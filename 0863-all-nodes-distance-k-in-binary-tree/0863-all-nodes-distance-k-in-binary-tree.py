# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
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
        
        Q = deque()
        Q.append(target.val)
        level = 0
        visited = {target.val}
        
        while Q:
            S = len(Q)
            
            if level == k:
                return list(Q)
            
            for _ in range(S):
                node = Q.popleft()
                for nei in G[node]:
                    if nei not in visited:
                        Q.append(nei)
                        visited.add(nei)
            level += 1
            
        return []
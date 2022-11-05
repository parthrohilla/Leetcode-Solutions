class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)   
        Q = deque()
        Q.append([0,0,0]) #[node, rotations, current_index]
        visited = set()
        
        while Q:
            i, rotations, current = Q.popleft()
            
            if (i, current) in visited:
                continue
            
            visited.add((i,current))
            
            while current < len(key) and key[current] == ring[i]:
                current += 1
            
            if current == len(key):
                clicks = len(key)
                return rotations + clicks
                
            if i == 0:
                Q.append([i+1, rotations + 1, current])
                Q.append([n-1, rotations + 1, current])
            elif i == n-1:
                Q.append([i-1, rotations + 1, current])
                Q.append([0, rotations + 1, current])
            else:
                Q.append([i+1, rotations + 1, current])
                Q.append([i-1, rotations + 1, current])
                
                
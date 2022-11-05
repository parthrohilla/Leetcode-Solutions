class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
            
        Q = deque()
        Q.append([0,0,0]) #[node, rotations, found_word]
        visited = set()
        
        while Q:
            i, rotations, found = Q.popleft()
            
            if (i, found) in visited:
                continue
            
            visited.add((i,found))
            
            while found < len(key) and key[found] == ring[i]:
                found += 1
            
            if found == len(key):
                return rotations + len(key)
                
            if i == 0:
                Q.append([i+1, rotations + 1, found])
                Q.append([n-1, rotations + 1, found])
            elif i == n-1:
                Q.append([i-1, rotations + 1, found])
                Q.append([0, rotations + 1, found])
            else:
                Q.append([i+1, rotations + 1, found])
                Q.append([i-1, rotations + 1, found])
        
        return -1
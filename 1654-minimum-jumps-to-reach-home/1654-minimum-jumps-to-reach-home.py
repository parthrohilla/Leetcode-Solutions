class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0: return 0
        
        forbidden = set(forbidden)
        Q = deque()
        Q.append([0,0])
        threshold = max(forbidden) + x + a + b
        visited = {0}
        while Q:
            curr, steps = Q.popleft()
            if (curr + a) not in visited and (curr + a) not in forbidden and (curr + a) <= threshold:
                if curr + a  == x: return steps + 1
                Q.append([curr+a, steps+1])
                visited.add(curr+a)
            
            if curr - b > 0 and (curr - b) not in forbidden and (curr - b ) not in visited:
                if curr - b == x: return steps + 1
                visited.add(curr-b)
                
                if (curr +a - b) not in visited and (curr + a - b) not in forbidden and (curr+a-b) <= threshold:
                    if curr +a - b == x: return steps + 2
                    visited.add(curr+a-b)
                    Q.append([curr + a - b, steps + 2])
            
        return -1
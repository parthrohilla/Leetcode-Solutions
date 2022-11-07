class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        Q = deque()
        Q.append([0,0,True])
        threshold = max(forbidden) + x + a + b
        visited = {(0,True)}
        while Q:
            curr, steps, flag = Q.popleft()
            
            if curr == x:
                return steps
            
            if (curr + a, False) not in visited and (curr + a) not in forbidden and (curr + a) <= threshold:
                Q.append([curr+a, steps+1, False])
                visited.add((curr+a, False))
            
            if curr - b > 0 and (curr - b) not in forbidden and (curr - b, flag) not in visited and not flag:
                Q.append([curr-b,steps + 1,True])
                visited.add((curr-b, True))
                         
        return -1
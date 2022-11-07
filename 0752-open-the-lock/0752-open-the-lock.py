class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        Q = deque()
        
        Q.append(["0000",0])
        
        visited = set()
        visited.add("0000")
        
        while Q:
            curr, steps = Q.popleft()
            
            if curr == target:
                return steps
            
            if curr in deadends:
                continue
            
            for i in range(4):
                digit = int(curr[i])
                for d in [-1,1]:
                    new_digit = (digit + d) % 10
                    new_state = curr[:i] + str(new_digit) + curr[i+1:]
                    if new_state not in visited:
                        Q.append([new_state, steps + 1])
                        visited.add(new_state)
                    
        return -1
                    
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        seen, Q = [False]*1001, deque()
        Q.append([start,0])
        seen[start] = True
        
        while Q:
            curr, operations = Q.popleft()
            
            for n in nums:
                new_states = [curr + n, curr - n, curr ^ n]
                
                for S in new_states:
                    
                    if S == goal:
                        return operations + 1
                    
                    if 0<=S<=1000 and not seen[S]:
                        Q.append([S, operations + 1])
                        seen[S] = True
            
        return -1

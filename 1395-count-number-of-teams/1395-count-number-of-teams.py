class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n, count = len(rating), 0
        for i,val in enumerate(rating):
            ls,rs,ll,rl = 0,0,0,0
            for j in rating[:i]:
                if j < val: ls += 1
                if j > val: ll += 1
            for j in rating[i+1:]:
                if j < val: rs += 1
                if j > val: rl += 1
            count += ls * rl
            count += ll * rs
        return count
            
        
        
        
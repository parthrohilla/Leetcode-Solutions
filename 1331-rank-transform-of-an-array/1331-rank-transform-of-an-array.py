class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0: 
            return arr
        
        sort, rank = sorted(arr), 1
        place = {sort[0]:rank}
        for i,num in enumerate(sort):
            if i >= 1 and sort[i] > sort[i-1]: rank += 1
            place[num] = rank
        
        return [place[x] for x in arr]
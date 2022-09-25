class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [names[i] for _,i in sorted([[num,i] for i,num in enumerate(heights)])[::-1]]
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp = sorted([[num,i] for i,num in enumerate(heights)])[::-1]
        ans = []
        for _,i in temp:
            ans.append(names[i])
        return ans
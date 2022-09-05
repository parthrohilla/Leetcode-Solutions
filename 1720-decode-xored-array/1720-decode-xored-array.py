class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        temp = first
        for num in encoded:
            temp = temp ^ num
            ans.append(temp)
        return ans
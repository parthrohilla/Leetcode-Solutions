class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [""]*len(s)
        for char,i in zip(s,indices):
            ans[i] = char
        return "".join(ans)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for i in range(1, len(strs)):
            temp, x = strs[i], ""
            for j in range(len(common)):
                if j<len(common) and j <len(temp) and common[j] == temp[j]:
                    x += common[j]
                else:
                    break
            common = x
        return common
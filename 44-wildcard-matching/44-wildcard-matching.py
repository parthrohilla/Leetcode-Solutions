class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(p), len(s)
        lookup = {}
        def dfs(i,j):
            # Base Cases
            if (i,j) in lookup: return lookup[(i,j)]
            if i < 0 and j < 0: return True
            if i < 0 and j >= 0: return False
            if i >= 0 and j < 0:
                if "".join(["*"]*(i+1)) == p[:i+1]: return True
                else: return False
            # Recursive Calls
            if p[i] == s[j] or p[i] == "?": lookup[(i,j)] = dfs(i-1,j-1)
            elif p[i] == "*": lookup[(i,j)] = dfs(i,j-1) or dfs(i-1,j)
            else: lookup[(i,j)] = False
            return lookup[(i,j)]
        return dfs(m-1,n-1)
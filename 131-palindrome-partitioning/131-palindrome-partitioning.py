class Solution:
    def partition(self, s):

        def dfs(string, path):
            if not string:
                output.append(path)
                return
            for i in range(len(string)):
                if self.isPal(string[:i+1]):
                    dfs(string[i+1:], path + [string[:i+1]])

        output = []
        dfs(s, [])
        return output

    def isPal(self, s):
        return s == s[::-1]
        
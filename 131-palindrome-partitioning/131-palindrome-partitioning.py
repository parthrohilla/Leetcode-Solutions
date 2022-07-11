class Solution:
    def partition(self, s):

        def dfs(string, path):
            if not string:
                output.append(path)
                return

            for i in range(1, len(string) + 1):
                if self.isPal(string[:i]):
                    dfs(string[i:], path + [string[:i]])

        output = []
        dfs(s, [])
        return output

    def isPal(self, s):
        return s == s[::-1]
        
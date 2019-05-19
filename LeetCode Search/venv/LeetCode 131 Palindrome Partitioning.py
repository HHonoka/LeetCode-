class Solution:
    def partition(self, s: str):
        self.res = []
        self.dfs(s, [])
        return self.res
    def dfs(self, s, path):
        if not s:
            self.res.append(path)
        for i in range(len(s)):
            cur = s[:i + 1]
            if cur == cur[::-1]:
                self.dfs(s[i + 1:], path + [cur])
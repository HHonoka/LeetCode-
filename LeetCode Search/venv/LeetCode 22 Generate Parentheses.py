class Solution:
    def generateParenthesis(self, n: int):
        self.res = []
        self.dfs(n, n, "")
        return self.res
    def dfs(self, l, r, path):
        if l == 0 and r == 0:
            self.res.append(path)
        if l > 0:
            self.dfs(l - 1, r, path + '(')
        if r > 0 and r > l:
            self.dfs(l, r - 1, path + ')')
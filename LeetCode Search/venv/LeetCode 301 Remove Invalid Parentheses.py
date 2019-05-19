class Solution:
    def removeInvalidParentheses(self, s: str):
        l, r = 0, 0
        for e in s:
            if e == '(':
                l += 1
            if e == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1
        self.ans = []
        self.dfs(s, l, r, 0)
        return self.ans
    def valid(self, s):
        count = 0
        for e in s:
            if e == '(':
                count += 1
            if e == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0
    def dfs(self, s, l, r, index):
        if l == 0 and r == 0 and self.valid(s):
            self.ans.append(s)
            return
        for i in range(index, len(s)):
            if i > index and s[i] == s[i - 1]:
                continue
            if s[i] == '(' or s[i] == ')':
                if r > 0 and s[i] == ')':
                    self.dfs(s[:i] + s[i + 1:], l, r - 1, i)
                elif l > 0 and s[i] == '(':
                    self.dfs(s[:i] + s[i + 1:], l - 1, r, i)
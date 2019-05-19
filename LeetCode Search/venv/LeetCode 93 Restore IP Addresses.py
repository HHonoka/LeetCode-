class Solution:
    def restoreIpAddresses(self, s: str):
        self.res = []
        self.dfs(s, [])
        return self.res
    def dfs(self, s, path):
        if len(s) > (4 - len(path))*3:
            return
        if not s and len(path) == 4:
            self.res.append('.'.join(path))
        for i in range(min(3, len(s))):
            cur = s[:i + 1]
            if (cur[0] == '0' and len(cur) >= 2) or int(cur) > 255:
                continue
            self.dfs(s[i + 1:], path + [cur])
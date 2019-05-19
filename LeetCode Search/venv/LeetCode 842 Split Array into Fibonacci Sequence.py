class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        self.res = []
        self.dfs(S, [])
        return self.res
    def dfs(self, S, path):
        if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
            return False
        if not S and len(path) >= 3:
            self.res.extend(path)
            return True
        for i in range(len(S)):
            cur = S[:i + 1]
            if (cur[0] == '0' and len(cur) > 1) or int(cur) >= 2**31 - 1:
                break #continue is also ok but slow.
            if self.dfs(S[i + 1:], path + [int(cur)]):
                return True
        return False
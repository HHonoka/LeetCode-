class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.res = []
        self.dfs(num, target, 0, 0, "")
        return self.res
    def dfs(self, num, target, pre, cur, path):
        if cur == target and not num:
            self.res.append(path)
        for i in range(len(num)):
            c = num[:i + 1]
            if (c[0] == '0' and len(c) > 1) or int(c) > 2**31 - 1:
                break
            if not path:
                self.dfs(num[i + 1:], target, int(c), int(c), c)
                continue
            self.dfs(num[i + 1:], target, int(c), cur + int(c), path + '+' + c)
            self.dfs(num[i + 1:], target, -int(c), cur - int(c), path + '-' + c)
            self.dfs(num[i + 1:], target, pre*int(c), cur - pre + pre*int(c), path + '*' + c)#***********************


#The most important problem for this question if how to solve the multiplication part.
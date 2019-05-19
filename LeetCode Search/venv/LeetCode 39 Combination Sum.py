class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(candidates, target, [], 0)
        return self.res

    def dfs(self, d, count, path, index):
        if count == 0:
            self.res.append(path)
            return
        for i in range(index, len(d)):
            if d[i] > count:
                continue
            self.dfs(d, count - d[i], path + [d[i]], i)

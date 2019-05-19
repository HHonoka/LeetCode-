class Solution:
    def combinationSum2(self, candidates, target: int):
        self.res = []
        candidates = [c for c in candidates if c <= target]
        candidates.sort()
        self.dfs(candidates, target, [], 0)
        return self.res
    def dfs(self, d, count, path, index):
        if count == 0:
            self.res.append(path)
            return
        for i in range(index, len(d)):
            if i > index and d[i] == d[i - 1]:
                continue
            if d[i] > count:
                break
            self.dfs(d, count - d[i], path + [d[i]], i + 1)
#DFS + Pruning
class Solution:
    def combine(self, n: int, k: int):
        self.res = []
        nums = [i for i in range(1, n + 1)]
        self.dfs(nums, k, [], 0)
        return self.res

    def dfs(self, nums, k, path, index):
        if k > len(nums) - index:
            return
        if k == 0:
            self.res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, k - 1, path + [nums[i]], i + 1)
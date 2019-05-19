class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        self.res = []
        self.dfs(nums, k, n, 0, [])
        return self.res
    def dfs(self, nums, k, n, index, path):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            self.res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, k - 1, n - nums[i], i + 1, path + [nums[i]])
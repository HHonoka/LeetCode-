class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        seen = [False] * len(nums)
        self.res = []
        self.dfs(nums, [], 0, seen)
        return self.res
    def dfs(self, nums, path, index, seen):
        self.res.append(path)
        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and seen[i - 1] == False:
                continue
            seen[i] = True
            self.dfs(nums, path + [nums[i]], i + 1, seen)
            seen[i] = False
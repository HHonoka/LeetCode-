class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        nums.sort(reverse = True)
        target = total // k
        if nums[0] > target:
            return False
        if k > len(nums):
            return False
        seen = [0]*len(nums)
        return self.dfs(k, 0, nums, target, 0, seen)
    def dfs(self, count, index, nums, target, ssum, seen):
        if count == 1:
            return True
        if ssum == target:
            return self.dfs(count - 1, 0, nums, target, 0, seen)
        for i in range(index, len(nums)):
            if not seen[i] and ssum + nums[i] <= target:
                seen[i] = 1
                if self.dfs(count, i + 1,nums, target, ssum + nums[i], seen):
                    return True
                seen[i] = 0
        return False
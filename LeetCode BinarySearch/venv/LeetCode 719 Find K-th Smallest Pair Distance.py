class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            count = 0
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and abs(nums[i] - nums[j]) <= mid:
                    j += 1
                count += (j - i - 1)
            if count >= k:
                r = mid
            else:
                l = mid + 1
        return l
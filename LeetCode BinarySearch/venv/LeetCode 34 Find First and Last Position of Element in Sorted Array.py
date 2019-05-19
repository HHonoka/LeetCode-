class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums):
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                a = mid
                b = mid
                while a > 0 and nums[a] == nums[a - 1]:
                    a -= 1
                while b < len(nums) - 1 and nums[b] == nums[b + 1]:
                    b += 1
                return [a, b]
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [-1, -1]
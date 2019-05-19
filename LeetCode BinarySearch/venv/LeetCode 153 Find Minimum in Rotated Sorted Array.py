class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r and nums[l] > nums[r]:
            mid = (l + r) // 2
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        return nums[l]




class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                return nums[l]
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
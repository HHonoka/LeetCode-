class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        k = (n1 + n2 + 1) // 2
        l = 0
        r = n1
        while l < r:
            m1 = (l + r) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                l = m1 + 1
            else:
                r = m1
        c1 = max(nums1[l - 1] if l > 0 else float('-inf'), nums2[k - l - 1] if (k - l) > 0 else float('-inf'))
        c2 = min(nums1[l] if l < n1 else float('inf'), nums2[k - l] if (k - l) < n2 else float('inf'))
        if (n1 + n2) % 2 == 1:
            return c1
        return (c1 + c2) * 0.5
#https://www.youtube.com/watch?v=KB9IcSCDQ9k
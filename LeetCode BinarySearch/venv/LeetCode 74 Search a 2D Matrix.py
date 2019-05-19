class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                a, b = 0, len(matrix[mid]) - 1
                while a <= b:
                    midd = (a + b) // 2
                    if matrix[mid][midd] == target:
                        return True
                    if matrix[mid][midd] > target:
                        b = midd - 1
                    if matrix[mid][midd] < target:
                        a = midd + 1
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
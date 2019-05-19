class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        ans = 0
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if j == 0 and i + 1 < m:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2
            if self.count(matrix, mid) >= k:
                r = mid
            else:
                l = mid + 1
        if self.count(matrix, r) >= k:
            return r
        if self.count(matrix, l) >= k:
            return l
        return -1

    def count(self, matrix, target):
        i = len(matrix) - 1
        j = 0
        res = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] <= target:
                j += 1
                res += (i + 1)
            else:
                i -= 1
        return res


n = len(str)
LCSRe = [[0 for x in range(n + 1)] for y in range(n + 1)]
res = ""
res_length = 0
index = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if (str[i - 1] == str[j - 1] and LCSRe[i - 1][j - 1] < (j - i)):
            LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1
            if (LCSRe[i][j] > res_length):
                res_length = LCSRe[i][j]
                index = max(i, index)
        else:
            LCSRe[i][j] = 0
    print(LCSRe)
if (res_length > 0):
    for i in range(index - res_length + 1, index + 1):
        res = res + str[i - 1]

return res
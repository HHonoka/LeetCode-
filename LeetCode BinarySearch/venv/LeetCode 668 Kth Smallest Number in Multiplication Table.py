class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        table = [[i * j for i in range(1, m + 1)] for j in range(1, n + 1)]
        stack = [(table[0][0], 0, 0)]
        res = 0
        for _ in range(k):
            res, i, j = heapq.heappop(stack)
            if j == 0 and i + 1 < len(table):
                heapq.heappush(stack, (table[i + 1][j], i + 1, j))
            if j + 1 < len(table[0]):
                heapq.heappush(stack, (table[i][j + 1], i, j + 1))
        return res

#Heap sort. TLE

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(x):
            ans = 0
            for i in range(1, m + 1):
                ans += min(x // i, n)
            return ans
        l = 1
        r = m * n
        while l < r:
            mid = (l + r) // 2
            print(mid)
            if count(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return l
#Binary Search
#Time complexity O(m * log (m * n))
#Space complexity O(1)
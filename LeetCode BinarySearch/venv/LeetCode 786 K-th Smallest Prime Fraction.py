class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        stack = [(A[0] / A[i], 0, i) for i in range(len(A) - 1, 0, -1)]
        for _ in range(K - 1):
            num, i, j = heapq.heappop(stack)
            i += 1
            if i < j:
                heapq.heappush(stack, (A[i] / A[j], i, j))
        return A[stack[0][1]], A[stack[0][2]]
#Heap

class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        l, r = 0, 1
        while l < r:
            mid = (l + r) / 2
            count = 0
            j = 1
            maxf = 0
            for i in range(len(A)):
                while j < len(A) and A[i]/A[j] > mid:
                    j += 1
                if j == len(A):
                    break
                count += len(A) - j
                f = A[i] / A[j]
                if f > maxf:
                    maxf = f
                    p = i
                    q = j
            if count == K:
                return A[p],A[q]
            if count < K:
                l = mid
            else:
                r = mid
        return []

#Binary Search
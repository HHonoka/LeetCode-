class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        A = [float('-inf')] + A + [float('-inf')]
        res = 0
        for i, e in enumerate(A):
            while stack and e < A[stack[-1]]:
                k = stack.pop()
                res += A[k] * (k - stack[-1]) * (i - k)
            stack.append(i)
        return res % (10 ** 9 + 7)

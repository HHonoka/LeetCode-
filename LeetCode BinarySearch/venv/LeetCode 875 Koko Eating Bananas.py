class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            count = 0
            for p in piles:
                if p <= mid:
                    count += 1
                else:
                    count += p // mid + 1
            if count > H:
                l = mid + 1
            else:
                r = mid
        return l
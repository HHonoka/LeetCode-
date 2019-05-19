class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        stack = [(grid[0][0], 0, 0)]
        res = 0
        seen = set((0, 0))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while stack:
            t, i, j = heapq.heappop(stack)
            res = max(res, t)
            if i == j == len(grid) - 1:
                break
            for x, y in directions:
                newi = i + x
                newj = j + y
                if 0 <= newi < len(grid) and 0 <= newj < len(grid) and (newi, newj) not in seen:
                    heapq.heappush(stack, (grid[newi][newj], newi, newj))
                    seen.add((newi, newj))
        return res
#Heap sort

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        l = grid[0][0]
        r = len(grid) * len(grid)
        self.grid = grid
        while l < r:
            mid = (l + r) // 2
            if self.check(mid):
                r = mid
            else:
                l = mid + 1
        return l

    def check(self, target):
        stack = [(0, 0)]
        seen = set((0, 0))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while stack:
            i, j = stack.pop()
            if i == j == len(self.grid) - 1:
                return True
            for x, y in directions:
                newi = i + x
                newj = j + y
                if 0 <= newi < len(self.grid) and 0 <= newj < len(self.grid) and (newi, newj) not in seen and \
                        self.grid[newi][newj] <= target:
                    stack.append((newi, newj))
                    seen.add((newi, newj))
        return False
#Binary Search
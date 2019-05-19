class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.dic = collections.defaultdict(int)
        self.c = 2
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.count = 0
                    self.dfs(grid, i, j)
                    self.dic[self.c] = self.count
                    res = max(res, self.count)
                    self.c += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.seen = set()
                    self.area = 0
                    self.getarea(grid, i, j)
                    res = max(res, self.area + 1)
        return res
    def dfs(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            self.count += 1
            grid[i][j] = self.c
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)
    def getarea(self, grid, i, j):
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] > 1 and grid[x][y] not in self.seen:
                self.area += self.dic[grid[x][y]]
                self.seen.add(grid[x][y])
class Solution:
    def shortestBridge(self, A) -> int:
        def dfs(i, j, island):
            if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] != 1:
                return
            A[i][j] = 2
            island.append((i, j))
            dfs(i + 1, j, island)
            dfs(i - 1, j, island)
            dfs(i, j + 1, island)
            dfs(i, j - 1, island)
        island = []
        flag = True
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1 and flag:
                    dfs(i, j, island)
                    flag = False
        step = 0

        while island:
            _len = len(island)
            for _ in range(_len):
                i, j = island.pop(0)
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x < 0 or y < 0 or x >= len(A) or y >= len(A[0]) or A[x][y] == 2:
                        continue
                    if A[x][y] == 1:
                        return step
                    A[x][y] = 2
                    island.append((x, y))
            step += 1
        return -1
#DFS + BFS
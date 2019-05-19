class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        path = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 0:
                    path.append((forest[i][j], i, j))
        path.sort()
        x, y = 0, 0
        res = 0
        while path:
            target, i, j = path.pop(0)
            move = self.bfs(x, y, target, forest)
            if move == -1:
                return -1
            res += move
            x, y = i, j
        return res
    def bfs(self, i, j, target, forest):
        queue = collections.deque([(i, j, 0)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        seen.add((i, j))
        while queue:
            x, y, step = queue.popleft()
            if forest[x][y] == target:
                return step
            for d1, d2 in directions:
                newx = x + d1
                newy = y + d2
                if 0 <= newx < len(forest) and 0 <= newy < len(forest[0]) and (newx, newy) not in seen:
                    if forest[newx][newy]:
                        queue.append((newx, newy, step + 1))
                        seen.add((newx, newy))
        return -1

#TLE, But I think this code is correct. 
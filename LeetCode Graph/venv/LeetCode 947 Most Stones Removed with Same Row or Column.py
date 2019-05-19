class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        seen = set()
        count = 0
        for i, j in stones:
            seen.add((i, j))
            rows[i].append(j)
            cols[j].append(i)
        def dfs(i, j):
            seen.discard((i, j))
            for x in rows[i]:
                if (i, x) in seen:
                    dfs(i, x)
            for y in cols[j]:
                if (y, j) in seen:
                    dfs(y, j)
        for i, j in stones:
            if (i, j) in seen:
                dfs(i, j)
                count += 1
        return len(stones) - count
class Solution:
    def solveNQueens(self, n: int):
        def backtrack(count):
            if count == 0:
                ans.append(list(grid))
            for i in range(n):
                if i not in cols and (i + len(grid)) not in diag and (i - len(grid) + n - 1) not in mdiag:
                    cols.add(i)
                    diag.add(i + len(grid))
                    mdiag.add(i - len(grid) + n - 1)
                    grid.append("."*(i)+"Q"+"."*(n-i-1))
                    backtrack(count - 1)
                    grid.pop()
                    cols.remove(i)
                    diag.remove(i + len(grid))
                    mdiag.remove(i - len(grid) + n - 1)
        diag = set()
        mdiag = set()
        cols = set()
        ans = []
        grid = []
        count = n
        backtrack(count)
        return ans
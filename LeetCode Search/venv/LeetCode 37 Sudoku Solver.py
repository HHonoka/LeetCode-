class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        seen = collections.deque([])
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i // 3)*3 + j // 3].add(board[i][j])
                else:
                    seen.append((i, j))
        def search():
            if not seen:
                return True
            r, c = seen[0]
            box = (r // 3)*3 + c // 3
            for num in nums:
                if num not in rows[r] and num not in cols[c] and num not in boxes[box]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)
                    seen.popleft()
                    if search():
                        return True
                    else:
                        board[r][c] = '.'
                        rows[r].discard(num)
                        cols[c].discard(num)
                        boxes[box].discard(num)
                        seen.appendleft((r, c))
            return False
        search()
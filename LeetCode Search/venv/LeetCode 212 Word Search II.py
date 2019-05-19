class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dic = {}
        self.res = set()
        for word in words:
            curnode = dic
            for c in word:
                if c in curnode:
                    curnode = curnode[c]
                else:
                    curnode[c] = {}
                    curnode = curnode[c]
            curnode['end'] = None
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in dic:
                    self.dfs(board, i, j, dic, "")
        return list(self.res)

    def dfs(self, board, i, j, node, path):
        if 'end' in node:
            self.res.add(path)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] not in node or board[i][j] == '#':
            return
        tmp = board[i][j]
        board[i][j] = '#'
        self.dfs(board, i + 1, j, node[tmp], path + tmp)
        self.dfs(board, i - 1, j, node[tmp], path + tmp)
        self.dfs(board, i, j + 1, node[tmp], path + tmp)
        self.dfs(board, i, j - 1, node[tmp], path + tmp)
        board[i][j] = tmp

#Backtrack + Trie
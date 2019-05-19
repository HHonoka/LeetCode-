class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        for i in range(len(M)):
            if M[i][i] == 1:
                self.dfs(M, i)
                count += 1
        return count

    def dfs(self, M, node):
        for i in range(len(M[node])):
            if M[node][i] == 1:
                M[node][i] = M[i][node] = 0
                self.dfs(M, i)
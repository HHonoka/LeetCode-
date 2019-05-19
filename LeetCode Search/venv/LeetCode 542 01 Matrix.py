class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    top = matrix[i - 1][j] + 1 if i > 0 else float('inf')
                    left = matrix[i][j - 1] + 1 if j > 0 else float('inf')
                    matrix[i][j] = min(top, left)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j]:
                    bottom = matrix[i + 1][j] + 1 if i < m - 1 else float('inf')
                    right =  matrix[i][j + 1] + 1 if j < n - 1 else float('inf')
                    matrix[i][j] = min(bottom, right, matrix[i][j])
        return matrix
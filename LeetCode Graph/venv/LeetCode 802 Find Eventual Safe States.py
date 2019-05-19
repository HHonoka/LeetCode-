class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        seen = [0]*len(graph)
        res = []
        def dfs(node):
            if seen[node] == -1:
                return False
            if seen[node] == 1:
                return True
            seen[node] = -1
            for n in graph[node]:
                if not dfs(n):
                    return False
            seen[node] = 1
            res.append(node)
            return True
        for i in range(len(graph)):
            if not dfs(i):
                continue
        return sorted(res)
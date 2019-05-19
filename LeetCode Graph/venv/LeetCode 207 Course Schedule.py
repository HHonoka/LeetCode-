class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = collections.defaultdict(list)
        for p in prerequisites:
            dic[p[0]].append(p[1])
        seen = [0] * (numCourses)

        def dfs(node):
            if seen[node] == 1:
                return True
            if seen[node] == -1:
                return False
            seen[node] = -1
            for i in dic[node]:
                if not dfs(i):
                    return False
            seen[node] = 1
            return True

        for i in range(numCourses):
            print(seen)
            if not dfs(i):
                return False
        return True
#Find Cycle
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = collections.defaultdict(set)
        dic1 = collections.defaultdict(set)
        for course in prerequisites:
            dic[course[0]].add(course[1])
            dic1[course[1]].add(course[0])
        stack = [i for i in range(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop(0)
            res.append(node)
            for i in dic1[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
        return res if len(res) == numCourses else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = collections.defaultdict(list)
        for p in prerequisites:
            dic[p[1]].append(p[0])
        seen = [0] * numCourses

        def dfs(node):
            if seen[node] == -1:
                return False
            if seen[node] == 1:
                return True
            seen[node] = -1
            for i in dic[node]:
                if not dfs(i):
                    return False
            self.path.append(node)
            seen[node] = 1
            return True

        self.path = []
        for i in range(numCourses):
            if not dfs(i):
                return []
        return self.path[::-1]

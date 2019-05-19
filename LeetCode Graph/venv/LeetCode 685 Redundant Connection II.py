class UnionFindSet:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]

    def find(self, u):
        while u != self.parents[u]:
            self.parents[u] = self.parents[self.parents[u]]
            u = self.parents[u]
        return u

    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)
        if x == y:
            return False
        self.parents[x] = self.parents[y]
        return True


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        ans1, ans2, dic = None, None, {}
        for n1, n2 in edges:
            if n2 in dic:
                ans1 = dic[n2]
                ans2 = [n1, n2]
                break
            dic[n2] = [n1, n2]
        s = UnionFindSet(len(edges))
        for n1, n2 in edges:
            if [n1, n2] == ans2:
                continue
            if not s.union(n1, n2):
                if ans1:
                    return ans1
                return [n1, n2]
        return ans2
class UnionFindSet:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.ranks = [1 for _ in range(n + 1)]

    def find(self, u):
        while u != self.parents[u]:
            self.parents[u] = self.parents[self.parents[u]]
            u = self.parents[u]
            print(self.parents)
            print(self.ranks)
        return u

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        else:
            self.parents[pv] = pu
            self.ranks[pu] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        s = UnionFindSet(len(edges))
        for edge in edges:
            if not s.union(edge[0], edge[1]):
                return edge
        return None

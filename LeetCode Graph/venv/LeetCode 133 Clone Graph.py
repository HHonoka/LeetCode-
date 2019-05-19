"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.dic = collections.defaultdict(list)
        newgraph = self.dfs(node)
        return newgraph
    def dfs(self, node):
        if not node:
            return
        if node in self.dic:
            return self.dic[node]
        copynode = Node(node.val, [])
        self.dic[node] = copynode
        for n in node.neighbors:
            copyn = self.dfs(n)
            if copyn:
                copynode.neighbors.append(copyn)
        return copynode
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            temp = []
            ans = []
            for node in stack:
                ans.append(node.val)
                if node.children:
                    temp.extend(node.children)
            res.append(ans)
            stack = temp
        return res
#Iteratively
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.res = []
        self.helper(root, 0)
        return self.res
    def helper(self, node, level):
        if node:
            if level + 1 > len(self.res):
                self.res.append([])
            self.res[level].append(node.val)
            if node.children:
                for n in node.children:
                    self.helper(n, level + 1)
#Recursive
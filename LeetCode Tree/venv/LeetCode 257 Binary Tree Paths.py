# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        self.dfs(root, "")
        return self.res
    def dfs(self, node, path):
        if node:
            if not node.left and not node.right:
                self.res.append(path + str(node.val))
            else:
                self.dfs(node.left, path + str(node.val)  + "->")
                self.dfs(node.right, path + str(node.val) + "->")
#Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        stack = [(root,"")]
        while stack:
            node,l = stack.pop()
            if not node.left and not node.right:
                res.append(l + str(node.val))
            if node.left:
                stack.append((node.left,l + str(node.val) + "->"))
            if node.right:
                stack.append((node.right,l + str(node.val) + "->"))
        return res

#Iteratively
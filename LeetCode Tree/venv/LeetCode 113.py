# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.dfs(root, [root.val], res, target)
        return res
    def dfs(self, node, path, res, target):
        if sum(path) == target and not node.left and not node.right:
            res.append(path)
        if node.left:
            self.dfs(node.left, path + [node.left.val], res, target)
        if node.right:
            self.dfs(node.right, path + [node.right.val], res, target)
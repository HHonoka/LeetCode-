# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.dic = collections.defaultdict(int)
        self.res = 0
        self.dic[0] = 1
        self.dfs(root, 0, sum)
        return self.res
    def dfs(self, node, count, target):
        if node:
            count += node.val
            self.res += self.dic[count - target]
            self.dic[count] += 1
            self.dfs(node.left, count, target)
            self.dfs(node.right,count, target)
            self.dic[count] -= 1
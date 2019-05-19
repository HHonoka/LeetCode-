# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            temp = []
            ans = []
            for node in stack:
                ans.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            stack = temp
            res.append(ans)
        return res

#Iteratively

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res = []
        self.helper(root, 0)
        return self.res

    def helper(self, node, level):
        if node:
            if level + 1 > len(self.res):
                self.res.append([])
            self.res[level].append(node.val)
            self.helper(node.left, level + 1)
            self.helper(node.right, level + 1)
#Recursive
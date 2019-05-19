# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if not node1 and not node2:
                continue
            if (node1 and not node2) or (not node1 and node2) or(node1.val != node2.val):
                return False
            if node1 and node2:
                stack1.append(node1.left)
                stack1.append(node1.right)
                stack2.append(node2.left)
                stack2.append(node2.right)
        return True if not stack1 and not stack2 else False

#Iteratively
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def helper(p, q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False
            if p and q:
                if p.val != q.val:
                    return False
            return helper(p.left, q.left) and helper(p.right, q.right)
        return helper(p, q)

#Recursive
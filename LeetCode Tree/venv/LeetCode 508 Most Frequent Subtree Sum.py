# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        count = collections.Counter()
        def helper(node):
            if not node:
                return 0
            v = node.val + helper(node.left) + helper(node.right)
            count[v] += 1
            return v
        helper(root)
        res = []
        fre = max(count.values())
        return [i for i in count.keys() if count[i] == fre]
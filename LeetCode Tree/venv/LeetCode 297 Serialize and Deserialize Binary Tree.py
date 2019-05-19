# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def helper(node):
            res.append(str(node.val) if node else '#')
            if node:
                helper(node.left)
                helper(node.right)

        helper(root)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(val for val in data.split())

        def helper():
            if vals:
                val = vals.popleft()
                if val == '#':
                    return None
                root = TreeNode(int(val))
                root.left = helper()
                root.right = helper()
                return root

        return helper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        res = []

        def preorder(node):
            if not node:
                return
            res.append(str(node.val))
            for child in node.children:
                preorder(child)
            res.append('#')

        preorder(root)
        return " ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        vals = [val for val in data.split()]
        queue = collections.deque(vals)
        if not queue:
            return
        root = Node(int(queue.popleft()), [])

        def helper(node):
            if not queue:
                return
            while queue[0] != '#':
                child = Node(int(queue.popleft()), [])
                node.children.append(child)
                helper(child)
            queue.popleft()

        helper(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
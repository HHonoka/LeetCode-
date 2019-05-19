"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dic = dict()
        dummy = Node(0, None, None)
        dic[head] = dummy
        copyhead = dummy
        cur = head
        while cur:
            node = Node(cur.val, cur.next, None)
            dic[cur] = node
            copyhead.next = node
            copyhead = copyhead.next
            cur = cur.next
        cur = head
        while cur:
            if cur.random:
                dic[cur].random = dic[cur.random]
            cur = cur.next
        return dummy.next
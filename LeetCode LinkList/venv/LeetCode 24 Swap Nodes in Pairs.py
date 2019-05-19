# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        p = dummy
        while head and head.next:
            node = head.next
            p.next = node
            head.next = node.next
            node.next = head
            p = p.next.next
            head = head.next
        return dummy.next
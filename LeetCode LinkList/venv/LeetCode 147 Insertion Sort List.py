# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        while head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                p = dummy
                temp = head.next
                head.next = head.next.next
                while p.next and p.next.val < temp.val:
                    p = p.next
                temp.next = p.next
                p.next = temp
        return dummy.next

# Insert sort
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mid = self.getmid(head)
        l = head
        r = mid.next
        mid.next = None
        return self.merge(self.sortList(l), self.sortList(r))
    def getmid(self, node):
        if not node:
            return node
        fast = slow = node
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    def merge(self, l, r):
        dummy = ListNode(0)
        p = dummy
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        if l:
            p.next = l
        if r:
            p.next = r
        return dummy.next

#The time complexity of this question has strict requirement.
#So we need to choose a good sort method.
#
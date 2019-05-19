# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head


#We should fing the point where fast node and slow node meet.
#Because fast node go through the path that are twice as long as slow node.
#The distance between head and point is equal to the distance between the slow node and point.

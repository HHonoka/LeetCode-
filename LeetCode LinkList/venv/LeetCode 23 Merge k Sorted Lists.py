# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        stack = []
        for i, node in enumerate(lists):
            if node:
                stack.append([node.val, i, node])
        heapq.heapify(stack)
        dummy = ListNode(0)
        p = dummy
        while stack:
            val, i, node = heapq.heappop(stack)
            p.next = ListNode(val)
            p = p.next
            if node.next:
                heapq.heappush(stack, [node.next.val, i, node.next])
        return dummy.next
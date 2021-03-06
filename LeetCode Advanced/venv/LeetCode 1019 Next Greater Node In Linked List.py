# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        stack = []
        res = [0]*len(nums)
        for i, e in enumerate(nums):
            while stack and nums[stack[-1]] < e:
                k = stack.pop()
                res[k] = e
            stack.append(i)
        return res
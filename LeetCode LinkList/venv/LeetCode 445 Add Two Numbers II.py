# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []
        num1 = 0
        num2 = 0
        num = []
        dummy = ListNode(0)
        node = dummy
        carry = 0
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        while s1 or s2:
            if s1:
                num1 = s1.pop()
            if s2:
                num2 = s2.pop()
            num.append((num1 + num2 + carry) % 10)
            carry = (num1 + num2 + carry) // 10
            num1 = 0
            num2 = 0
        if carry:
            num.append(carry)
        while num:
            node.next = ListNode(num.pop())
            node = node.next
        return dummy.next
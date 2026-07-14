# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        carry = 0

        solution = ListNode()
        p3 = solution

        while p1 or p2 or carry:
            if p1:
                pointer1 = p1.val
            else:
                pointer1 = 0
            
            if p2:
                pointer2 = p2.val
            else:
                pointer2 = 0

            value = pointer1 + pointer2

            if carry != 0:
                value += carry
                carry = 0
            
            if len(str(value)) > 1:
                carry = int(str(value)[0])
                value = int(str(value)[-1])

            node = ListNode(value)

            p3.next = node
            p3 = p3.next

            if p1:
                p1 = p1.next
            
            if p2:
                p2 = p2.next

        return solution.next

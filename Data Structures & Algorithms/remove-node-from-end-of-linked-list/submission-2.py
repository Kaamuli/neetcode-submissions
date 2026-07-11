# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p1,p2 = dummy,dummy

        N = 0 #Store the length of the linked list

        while p1:
            p1 = p1.next
            N += 1
        
        for i in range(N-n-1):
            p2 = p2.next
        
        current_node = p2
        p2 = p2.next.next

        current_node.next = p2

        return dummy.next
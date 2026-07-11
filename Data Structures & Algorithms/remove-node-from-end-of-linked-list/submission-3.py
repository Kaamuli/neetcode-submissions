# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode() #We introduce a dummy to handle the edge case of N==n, if you ever need to remove or modify the head of the list likely you need this
        dummy.next = head
        p1,p2 = dummy,dummy

        N = 0 #Store the length of the dummy + linked list

        while p1:
            p1 = p1.next
            N += 1
        
        for i in range(N-n-1): #Gets you 1 before the node you want to delete
            p2 = p2.next
        
        current_node = p2
        p2 = p2.next.next

        current_node.next = p2

        return dummy.next
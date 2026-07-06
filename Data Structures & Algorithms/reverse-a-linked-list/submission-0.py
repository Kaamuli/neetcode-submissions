# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #If linked list is empty
        if not head:
            return None

        newHead = head #Assumes current head is the head
        
        if head.next: #If there is a node ahead of it.
            newHead = self.reverseList(head.next)

            head.next.next = head
        head.next = None #Sets current head point to nothing

        return newHead
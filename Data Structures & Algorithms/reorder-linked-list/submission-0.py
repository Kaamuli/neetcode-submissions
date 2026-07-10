# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find the middle
        slow,fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next #Now slow is at middle, by time fast is at the end


        #Reverse the 2nd list
        second = slow.next
        prev = None #initialise the previous value as the head of the linked list pointing towards none
        slow.next = None #Points the current (initial node i.e. head) towards None to indicate at the end
        while second:
            nxt = second.next #Stores old link to next node
            second.next = prev
            prev = second #Keeps track of the node that we were 'just' at
            second = nxt #Pointer takes us to the next position

        #Merge the two linked lists

        pointer1,pointer2 = head, prev

        while pointer2:
            temp1,temp2 = pointer1.next, pointer2.next
            pointer1.next = pointer2
            pointer2.next = temp1
            pointer1 = temp1
            pointer2 = temp2
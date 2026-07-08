# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #Remembers where you started
        pointer = dummy #Pointer! Tells you where you are!!

        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next

            pointer = pointer.next
        
        if list1: #Simply connects because its not like an array visual drawing shows this but connects the sorted bit to the list that still has a node left as only a node references the next node
            pointer.next = list1
        elif list2:
            pointer.next = list2
        
        return dummy.next #Ignores the initial dummy position
        
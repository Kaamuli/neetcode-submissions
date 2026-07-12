"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p1, p2 = head,head

        hashmap = {None: None}
        while p2:
            hashmap[p2] = Node(p2.val)
            p2 = p2.next
        
        while p1:
            copy = hashmap[p1]

            copy.next = hashmap[p1.next]
            copy.random = hashmap[p1.random]
            p1 = p1.next
        
        return hashmap[head]
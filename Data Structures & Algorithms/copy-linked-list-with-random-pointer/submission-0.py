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
        curr = head
        d = {None: None}
        dummy = Node(0)
        p = dummy
        while curr:
            node = Node(curr.val)
            p.next = node
            p = node
            d[curr] = node
            curr = curr.next
        curr = head
        
        while curr:
            d[curr].random = d[curr.random]
            curr = curr.next
        return dummy.next
            

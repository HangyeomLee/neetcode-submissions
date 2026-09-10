# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count should not work because it is node base wait is it working? 
        dummy = ListNode(0, head)
        curr = dummy
        count = 0
        fast = curr
        slow = curr
        # use slow and fast method again and make the distance between slow and fast N and then just skip slow node
        while n + 1:
            n = n - 1
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

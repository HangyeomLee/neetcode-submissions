# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is in the middle
        prev = None
        end = slow
        while end:
            nxt = end.next
            end.next = prev
            prev = end
            end = nxt
        #prev is the one
        end = prev
        start = head
        start_end_state = 0
        dummy = ListNode(None)
        tail = dummy
        # now end is the one
        while start and end:
            if start_end_state == 0:
                start_end_state = 1
                tail.next = start
                start = start.next
            else:
                start_end_state = 0
                tail.next = end
                end = end.next
            tail = tail.next

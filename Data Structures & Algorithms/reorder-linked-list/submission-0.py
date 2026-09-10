# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # using slow and fast pointer method
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # necessity of fast link is done
        # now I have two interval 0~slow slow~1
        # 0~ slow maybe stays normal
        # slow ~ 1 might need reverse
        # slow ~ 1 reverse part
        prev = None
        end = slow
        while end:
            nxt = end.next
            end.next = prev
            prev = end
            end = nxt
        end = prev
        # after done reversing it we need to attach both
        start = head
        state = 0
        dummy = ListNode()
        tail = dummy
        while start and end:
            if state == 0:
                tail.next = start
                start = start.next
                state = 1
            else:
                state = 0
                tail.next = end
                end = end.next
            tail = tail.next
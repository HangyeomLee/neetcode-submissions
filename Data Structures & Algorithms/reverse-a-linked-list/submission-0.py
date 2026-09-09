# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next    # 다음 노드 보관
            curr.next = prev   # 화살표 뒤집기
            prev = curr        # prev 전진
            curr = nxt         # curr 전진
        
        return prev
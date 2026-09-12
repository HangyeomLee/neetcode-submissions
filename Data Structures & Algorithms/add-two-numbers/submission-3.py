# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = l1
        list2 = l2
        dummy = ListNode(0)
        tail = dummy
        carry_state = 0
        while list1 or list2:
            x = list1.val if list1 else 0
            y = list2.val if list2 else 0
            tail.next = ListNode(0)
            total = (x + y + carry_state) % 10
            carry_state = (x + y + carry_state) // 10
            tail.next.val = total
            tail = tail.next
            list1 = list1.next if list1 else 0
            list2 = list2.next if list2 else 0
        if carry_state != 0:
            tail.next = ListNode(0)
            tail.next.val = carry_state

        return dummy.next
            
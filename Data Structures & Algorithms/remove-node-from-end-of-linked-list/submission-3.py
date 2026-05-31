# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        prev  = head
        index = length - n
        if index == 0:
            return head.next
        while index > 1:
            prev = prev.next
            index -= 1
        curr = prev.next.next
        prev.next = curr
        return head
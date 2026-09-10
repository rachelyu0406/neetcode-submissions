# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # one pass solution (left is prev to head initially)
        dummy = ListNode(0, head)
        l = dummy
        r = head
        while n > 0 and r:
            r = r.next
            n -= 1
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next

        """
        # two pass solution
        cnt = 0 # length of linked list
        cur = head
        while cur:
            cur = cur.next
            cnt += 1
        if n == cnt:
            return head.next
        prev = head
        for i in range(cnt - n - 1):
            prev = prev.next
        nxt = prev.next.next
        prev.next = nxt
        return head
        """     
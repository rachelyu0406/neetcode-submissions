# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        carryOn = 0
        res = ListNode(0)
        start = res
        cur = res
        while cur1 and cur2:
            res.val = (cur1.val + cur2.val + carryOn) % 10
            res.next = ListNode(0)
            cur = res
            res = res.next
            carryOn = (cur1.val + cur2.val + carryOn) // 10
            cur1 = cur1.next
            cur2 = cur2.next
        if cur1:
            while cur1:
                cur.next = ListNode((cur1.val + carryOn) % 10)
                carryOn = (cur1.val + carryOn) // 10
                cur = cur.next
                cur1 = cur1.next
        elif cur2:
            while cur2:
                cur.next = ListNode((cur2.val + carryOn) % 10)
                carryOn = (cur2.val + carryOn) // 10
                cur = cur.next
                cur2 = cur2.next
        else:
            exit
        if carryOn != 0:
            cur.next = ListNode(carryOn)
        else:
            cur.next = None
            return start
        return start
        
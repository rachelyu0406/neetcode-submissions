# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
            
        if list1.val < list2.val:
            head = list1
            curr = head
            dummy1 = list1.next
            dummy2 = list2
        else:
            head = list2
            curr = head
            dummy1 = list1
            dummy2 = list2.next
        while dummy1 and dummy2:
            if dummy1.val < dummy2.val:
                head.next = dummy1
                head = dummy1
                dummy1 = head.next
            else:
                head.next = dummy2
                head = dummy2
                dummy2 = head.next
        if dummy1:
            head.next = dummy1
        if dummy2:
            head.next = dummy2
        return curr        
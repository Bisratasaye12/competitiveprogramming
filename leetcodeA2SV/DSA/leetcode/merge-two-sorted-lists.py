# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        l1, l2 = list1, list2
        h = l3 = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
            elif l1 == l2:
                l3.next = l1
                l3.next.next = l2
                l1 = l1.next
                l2 = l2.next
                l3 = l3.next.next
            else:
                l3.next = l2
                l2 = l2.next
                l3 = l3.next

        while l1:
            l3.next = l1
            l1 = l1.next
            l3 = l3.next
        while l2:
            l3.next = l2
            l2 = l2.next
            l3 = l3.next

        h = h.next
        return h

    

        
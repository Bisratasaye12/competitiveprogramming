# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new = head
        prev, nex = new, new.next
        res = None

        while nex:
            if prev.val == nex.val:

                prev.next = nex.next
                nex = nex.next
            else:
                prev = nex
                nex = nex.next

        return new

        
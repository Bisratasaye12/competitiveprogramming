# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None
        left, lcurr, right, rcurr = None, None, None, None

        curr = head
        
        while curr:
            if curr.val < x:
                if not left:
                    left = curr
                    lcurr = curr
                else:
                    lcurr.next = curr
                    lcurr = lcurr.next
            else:
                if not right:
                    right = curr
                    rcurr = curr
                else:
                    rcurr.next = curr
                    rcurr = rcurr.next
            curr = curr.next
        if rcurr:
            rcurr.next = None
        if lcurr:
            lcurr.next = right

        return right if not left else left
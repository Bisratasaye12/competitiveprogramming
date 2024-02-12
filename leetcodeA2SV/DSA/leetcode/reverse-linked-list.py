# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        tail = head
        if not head: return head
        while tail.next:
            tail = tail.next

        prev, curr, n = None, head, head.next

        while curr:
            curr.next = prev
            prev = curr
            curr = n
            if n:
                n = n.next

        return tail
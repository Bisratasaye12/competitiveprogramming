# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))
        dummy.next = head
        head = dummy

        prev, curr = head, head.next

        while curr:
            if curr.val < prev.val:
                temp = curr.next
                prev.next = curr.next

                nprev, ncurr = head, head.next
                while ncurr and ncurr.val < curr.val:
                    nprev = nprev.next
                    ncurr = ncurr.next

                nprev.next = curr
                curr.next = ncurr
                curr = temp     
            else:
                curr = curr.next
                prev = prev.next

        return head.next


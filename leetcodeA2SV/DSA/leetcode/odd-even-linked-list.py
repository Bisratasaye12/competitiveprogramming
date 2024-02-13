# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds, evens = ListNode(), ListNode()
        l,r = odds, evens

        curr = head
        odd = True

        while curr:
            temp = curr.next
            if odd:
                l.next = curr
                l = l.next
            else:
                r.next = curr
                r = r.next

            curr = temp
            odd = not odd

        print(odds)
        l.next = None
        r.next = None
        l.next = evens.next

        return odds.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(next= head)

        prev, curr = dummy, head

        for i in range(left-1):
            prev = curr
            curr = curr.next

        leftPrev = prev
        prev = None

        for i in range(right - left + 1):
                temp = curr.next
                curr.next = prev

                prev = curr
                curr = temp
               
        lft = leftPrev.next
        lft.next = curr # curr is now pointing at the next node of "right"
        leftPrev.next = prev # prev is now at the "right"

        return dummy.next




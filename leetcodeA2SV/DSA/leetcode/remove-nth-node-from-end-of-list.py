# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head

        l = 0

        while curr != None:
            l += 1
            curr = curr.next

        diff = l - n
        print(l,n,diff)

        if diff == 0:
            return head.next

        curr = head
        for i in range(diff-1):
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next

        return head


        
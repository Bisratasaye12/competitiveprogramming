# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        dec = 0

        while curr:
            dec = (dec * 2) + curr.val
            curr = curr.next

        return dec
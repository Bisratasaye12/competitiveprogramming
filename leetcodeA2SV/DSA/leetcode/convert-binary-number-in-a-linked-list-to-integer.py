# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sum = 0
        i = 1
        curr = head

        while curr.next != None:
            i *= 2
            curr = curr.next

        num = i #..........correction

        curr = head
        while curr != None:
            sum = sum + (curr.val * num)
            num = num // 2
            curr = curr.next

        return sum
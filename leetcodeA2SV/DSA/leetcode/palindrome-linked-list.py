# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:         
        if head == None:
            return False
        elif head.next == None:
            return True
        
        lst = []
        curr = head
        while curr != None:
            lst.append(curr.val)
            curr = curr.next

        if lst != lst[::-1]:
            return False
        return True

       
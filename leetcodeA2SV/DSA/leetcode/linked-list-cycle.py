# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False

        tort = head
        hare = head

        while tort and hare:            
            tort = tort.next
            if hare.next:
                hare = hare.next.next
            else:
                break

            if tort and hare:
                if tort == hare: return True

        return False

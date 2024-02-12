# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def rev(node, h=head):
            if node == None:
                return 
            if node.next == None:
                h = node
                return h
            h = rev(node.next)
            node.next.next = node
            node.next = None
            return h
        head = rev(head)
        return head
    
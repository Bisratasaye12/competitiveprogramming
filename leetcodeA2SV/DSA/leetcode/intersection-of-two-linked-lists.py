# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = 0, 0
        if not headA or not headB:
            return None

        curr1, curr2 = headA, headB

        while curr1.next:
            l1 += 1
            curr1 = curr1.next

        while curr2.next:
            l2 += 1
            curr2 = curr2.next

        l1 += 1
        l2 += 1
        if curr1 != curr2:
            print(curr1, curr2)
            return None

        curr1, curr2 = headA, headB
        diff = abs(l1 - l2)
        print(diff)
        if l1 < l2:
            for i in range(diff):
                curr2 = curr2.next
        elif l1 > l2:
            for j in range(diff):
                curr1 = curr1.next

        while curr1 and curr2:
            if curr1 == curr2:
                return curr1

            curr1 = curr1.next
            curr2 = curr2.next

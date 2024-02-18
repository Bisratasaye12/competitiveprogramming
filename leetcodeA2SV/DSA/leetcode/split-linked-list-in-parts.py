# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head: 
            return [None] * k

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        q, r = divmod(n, k)
        res_len = k

        res = []
        curr = head

        for i in range(k):
            size = q + 1 if i < r else q
            if size == 0:
                res.append(None)
            else:
                res.append(curr)
                for j in range(size - 1):
                    curr = curr.next
                tmp = curr.next
                curr.next = None
                curr = tmp

        return res

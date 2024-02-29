# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        mn = [float('-inf')]
        
        def kth(root):
            nonlocal k
            if k <= 0 or not root:
                return 

            kth(root.left)
            if k > 0:
                mn[0] = max(mn[0], root.val)
                k -= 1
            kth(root.right) 

        kth(root)
        return mn[0]
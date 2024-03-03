# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
       

        def preord(root):
            if not root:  
                return 0             
            
            _sum = 0

            if low <= root.val <= high:
                _sum += root.val

            left = preord(root.left)
            right = preord(root.right)

            return _sum + left + right

        return preord(root)
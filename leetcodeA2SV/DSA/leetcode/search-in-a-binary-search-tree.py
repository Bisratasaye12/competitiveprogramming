# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def search(root, val, ans= root):
            if not root:
                return 
            if root.val == val:
                ans = root
                return ans
            if val< root.val and root.left:
                return search(root.left, val)
            if val > root.val and root.right:
                return search(root.right, val)
            
        return search(root, val)
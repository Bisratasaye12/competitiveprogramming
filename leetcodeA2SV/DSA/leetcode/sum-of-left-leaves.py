# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        

        def sumLeft(parent, root):
            if not root:
                return 0

            left = sumLeft(root, root.left)
            right = sumLeft(root, root.right)

            if not root.left and not root.right and parent.left == root:
                return root.val + left + right
            else:
                return left + right

        return sumLeft(TreeNode(), root)

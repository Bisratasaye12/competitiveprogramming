# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def merge(root, root1, root2):
            if not root1 and not root2:
                return root
            elif not root1:
                return root2
            elif not root2:
                return root1

            root = TreeNode(root1.val + root2.val)
            root.left = merge(root.left, root1.left, root2.left)
            root.right = merge(root.right, root1.right, root2.right)

            return root

        return merge(None, root1, root2)
            


            
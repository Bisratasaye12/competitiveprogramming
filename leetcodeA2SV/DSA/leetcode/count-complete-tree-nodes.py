# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = [0]


        def levelOrder(root):
            if not root:
                return 

            if root.left : count[0] += 1
            if root.right : count[0] += 1

            levelOrder(root.left)
            levelOrder(root.right)

        levelOrder(root)
        return count[0] + 1 if root else 0 


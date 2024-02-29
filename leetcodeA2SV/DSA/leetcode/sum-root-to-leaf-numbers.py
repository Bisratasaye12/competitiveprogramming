# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        _sum = [0]

        def sumPath(root, path):
            if not root:
                return 

            path[0] = (path[0] * 10) + root.val
            sumPath(root.left, path)
            sumPath(root.right, path)
            if not root.left and not root.right:
                _sum[0] += path[0]
            path[0] //= 10

        sumPath(root, [0])

        return _sum[0]
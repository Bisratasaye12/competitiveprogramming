# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        def inord(root):
            if not root:
                return

            inord(root.left)
            inorder.append(root.val)
            inord(root.right)

        inord(root)

        def balance(root, nums):
            if not nums:
                return

            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = balance(root.left, nums[:mid])
            root.right = balance(root.right, nums[mid+1:])
            return root

        return balance(None, inorder)

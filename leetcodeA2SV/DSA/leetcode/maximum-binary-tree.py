# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        def build(root, elems):
            if not elems:
                return None

            mid = elems.index(max(elems))
            root = TreeNode(elems[mid])
            root.left = build(root.left, elems[:mid])
            root.right = build(root.right, elems[mid + 1:])
            return root

        return build(None, nums)



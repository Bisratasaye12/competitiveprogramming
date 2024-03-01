# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(list)

        def find(root, level, num):
            if not root:
                return

            d[level].append(num)
            find(root.left, level + 1, 2*num + 1)
            find(root.right, level + 1, 2*num + 2)


        find(root, 0, 0)
        mx = 0

        for level in d:
            if d[level]:
                mx = max(mx, d[level][-1] - d[level][0])

        return mx + 1


            

            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)

        def inorder(root):
            if not root:
                return 
            d[root.val] += 1
            inorder(root.left)
            inorder(root.right)

        inorder(root)
        modes = []
        mx = max(d.values())

        for i in d:
            if d[i] == mx:
                modes.append(i)

        return modes

            
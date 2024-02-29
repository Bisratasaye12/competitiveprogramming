# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)

        def traverse(root, col, row):
            if not root:
                return 

            d[col].append((root.val, row))
            traverse(root.left, col - 1, row + 1)
            traverse(root.right, col + 1, row + 1)

        traverse(root, 0,0)
        ans = []
        #print(d)
        for i in sorted(d):
            ans.append([j[0] for j in sorted( d[i], key= lambda x: (x[1], x[0]))])

        return ans
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)

        def zigzag(root, level):
            if not root:
                return 

            result[level].append(root.val)

            zigzag(root.left, level + 1)
            zigzag(root.right, level + 1)
        
        zigzag(root, 0)
        ans = [result[i] for i in sorted(result.keys())]

        for i in result:
            if i%2:
                ans[i] = result[i][::-1]
            else:
                ans[i] = result[i]

        return ans

            
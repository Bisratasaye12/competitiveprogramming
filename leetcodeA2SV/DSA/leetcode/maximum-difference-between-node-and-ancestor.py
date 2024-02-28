class Solution:
    def __init__(self):
        self.max_difference = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def find(root, minValue, maxValue):
            if root:
                minValue = min(minValue, root.val)
                maxValue = max(maxValue, root.val)
                self.max_difference = max(self.max_difference, maxValue - minValue)

                find(root.left, minValue, maxValue)
                find(root.right, minValue, maxValue)
        find(root, root.val, root.val)
        return self.max_difference

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = None

        def insert(root, nums):
            if not nums:
                return 

            idx = len(nums) // 2 
            root = TreeNode(nums[idx])
            root.left = insert(root.left, nums[:idx])
            root.right = insert(root.right, nums[idx+1:])
            return root

        return insert(root, nums)
            


            
           
        
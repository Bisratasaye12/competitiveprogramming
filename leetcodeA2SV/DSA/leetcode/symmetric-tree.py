# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        queue = deque([root.left, root.right])
        
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            
            if not left and not right:
                continue
            if not left and right:
                return False
            if not right and left:
                return False
            if left and right:
                if left.val != right.val:
                    return False
                queue.append(left.left)
                queue.append(right.right)
                queue.append(right.left)
                queue.append(left.right)
                
        return True
                
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = deque([root])
        count = 0
        while queue:
            flag = True
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    flag = False
                    if node.children:
                        for n in node.children:
                            queue.append(n)
                    else:
                        queue.append(node.children)
            if flag:
                return count
            else:
                count += 1

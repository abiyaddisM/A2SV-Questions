# May 23 2025
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            for i in range(len(root.children)):
                helper(root.children[i])
            res.append(root.val)
        helper(root)
        return res
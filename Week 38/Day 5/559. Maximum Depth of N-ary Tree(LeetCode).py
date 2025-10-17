# October 17 2025
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        def helper(cur, depth):
            if not cur:
                return depth
            res = depth
            for next in cur.children:
                res = max(res, helper(next, depth + 1))
            return res

        return helper(root, 1)
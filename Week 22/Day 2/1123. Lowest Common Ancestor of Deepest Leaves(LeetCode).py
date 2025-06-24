# June 24 2025
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.res = None
        self.max = 0

        def helper(root, depth):
            if not root:
                return depth
            l = helper(root.left, depth + 1)
            r = helper(root.right, depth + 1)
            print(l, r, root.val)
            if self.max <= l and self.max <= r:
                self.res = root
                self.max = l
            return max(l, r)

        helper(root, 0)
        return self.res

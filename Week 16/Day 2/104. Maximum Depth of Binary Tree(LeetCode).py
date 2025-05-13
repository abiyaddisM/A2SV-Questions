# May 13 2025
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], num = 0) -> int:
        if not root:
            return num
        return max(self.maxDepth(root.left, num + 1), self.maxDepth(root.right, num + 1))
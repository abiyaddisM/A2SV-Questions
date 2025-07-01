# July 1 2025
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(root, higher):
            if not root:
                return 0
            total = helper(root.right, higher)
            root.val += total
            if not root.right:
                root.val += higher
            left = helper(root.left, root.val)

            return max(left, root.val)

        helper(root, 0)
        return root
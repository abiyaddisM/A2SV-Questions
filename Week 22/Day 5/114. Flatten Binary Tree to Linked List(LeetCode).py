# June 26 2025
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=problem-list-v2&envId=depth-first-search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def helper(root):
            if not root:
                return
            rightLeaf = root.right
            left = helper(root.left)
            if left:
                left.right = root.right
                root.right = root.left
                root.left = None
            right = helper(root.right)
            if not left and not right:
                return root
            if not right:
                return left
            return right

        helper(root)
        return root

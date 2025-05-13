# May 13 2025
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode],arr = []) -> List[int]:
        def helper(root,arr):
            if not root:
                return
            arr.append(root.val)
            helper(root.left,arr)
            helper(root.right, arr)
        arr = []
        helper(root, arr)
        return arr
# May 14 2025
# https://leetcode.com/problems/delete-node-in-a-bst/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        def helper(root):
            while root.left:
                root = root.left
            return root.val
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            suc = helper(root.right)
            root.val = suc
            root.right = self.deleteNode(root.right, suc)
        return root

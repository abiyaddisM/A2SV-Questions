# May 13 2025
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            arr.append(root.val)

        helper(root)
        return arr
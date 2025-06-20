# June 20 2025
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def helper(root, path):
            if not root:
                return
            newPath = path + str(root.val)
            if not root.left and not root.right:
                res.append(int(newPath))
            helper(root.left, newPath)
            helper(root.right, newPath)

        helper(root, '')
        return sum(res)
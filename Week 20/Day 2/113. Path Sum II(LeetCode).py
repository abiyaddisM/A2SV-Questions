# June 10 2025
# https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def helper(root, total, path):
            if not root:
                return
            path.append(root.val)
            total += root.val
            if total == targetSum and not root.left and not root.right:
                res.append(path[:])
            helper(root.left, total, path)
            helper(root.right, total, path)
            path.pop()
        helper(root, 0, [])
        return res
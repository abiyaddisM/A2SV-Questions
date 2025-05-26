# May 26 2025
# https://leetcode.com/problems/path-sum/description/
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, total = 0) -> bool:
        if not root:
            return False

        total += root.val

        if not root.left and not root.right:
            return total == targetSum

        return self.hasPathSum(root.left, targetSum, total) or self.hasPathSum(root.right, targetSum, total)

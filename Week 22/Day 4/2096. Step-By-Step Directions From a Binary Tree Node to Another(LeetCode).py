# June 25 2025
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start = []
        dest = []

        def helper(root):
            if not root:
                return -1
            stemp = -1
            dtemp = -1

            if root.val == startValue:
                stemp = root.val
            if root.val == destValue:
                dtemp = root.val

            left = helper(root.left)
            right = helper(root.right)
            if left == startValue or right == startValue:
                start.append('U')
                stemp = startValue
            if left == destValue or right == destValue:
                dest.append('L' if left == destValue else 'R')
                dtemp = destValue
            if stemp == startValue and dtemp == destValue:
                return -1
            return max(stemp, dtemp)

        helper(root)
        dest.reverse()
        print(start, dest)

        return ''.join(start) + ''.join(dest)
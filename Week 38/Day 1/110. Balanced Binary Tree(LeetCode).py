# October 13 2025
# https://leetcode.com/problems/balanced-binary-tree/description/?roomId=FMTwVV
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def helper(cur, depth):
            if not cur:
                return depth

            t1 = helper(cur.left, depth + 1)
            t2 = helper(cur.right, depth + 1)
            if abs(t1 - t2) > 1:
                self.res = False
            # print(t1, t2)
            return max(t1, t2)

        helper(root, 0)
        return self.res
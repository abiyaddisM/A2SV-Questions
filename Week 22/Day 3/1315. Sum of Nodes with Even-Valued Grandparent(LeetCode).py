# June 25 2025
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def sumEven(root, depth):
            if not root:
                return 0
            if depth == 2:
                return root.val
            return sumEven(root.left, depth + 1) + sumEven(root.right, depth + 1)


        def helper(root):
            if not root:
                return
            if root.val % 2 == 0:
                self.res += sumEven(root, 0)
                print(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return self.res


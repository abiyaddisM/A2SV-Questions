# February 12 2025
# https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode],level = 0) -> int:
        def search(root,level):
            if not root:
                return [-1,-1]
            left = search(root.left,level + 1)
            right = search(root.right, level + 1)
            if left[1] == -1 and right[1] == -1:
                return [root.val,level]
            elif left[1] == -1:
                return right
            elif right[1] == -1:
                return left
            else:
                if right[1] > left[1]:
                    return right
                else:
                    return left
        return search(root,0)[0]
# June 16 2025
# https://leetcode.com/problems/binary-tree-paths/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def helper(root, path):
            if not root:
                return
            path.append(root.val)
            helper(root.left, path)
            helper(root.right, path)
            if not root.left and not root.right:
                temp = str(path[0])
                for i in range(1,len(path)):
                    temp += '->' + str(path[i])
                res.append(temp)
            path.pop()
        helper(root, [])
        return res
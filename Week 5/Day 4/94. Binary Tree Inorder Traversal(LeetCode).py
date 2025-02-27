# February 27 2025
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = self.inorderTraversal(root.left)
        res.append(root.val)
        res2 = self.inorderTraversal(root.right)
        res.extend(res2)
        return res


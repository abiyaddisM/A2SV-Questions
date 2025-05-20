# May 20 2025
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = {}
        def helper(root):
            if not root:
                return
            dic[root.val] = dic.get(root.val,0) + 1
            helper(root.left)
            helper(root.right)
        helper(root)
        max_freq = max(dic.values())
        return [val for val, freq in dic.items() if freq == max_freq]

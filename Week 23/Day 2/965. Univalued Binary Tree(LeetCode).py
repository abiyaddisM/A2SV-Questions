# July 1 2025
# https://leetcode.com/problems/univalued-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        que = deque([root])
        pre = root.val
        while que:
            size = len(que)
            for i in range(size):
                temp = que.popleft()
                if pre != temp.val:
                    return False
                pre = temp.val
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
        return True
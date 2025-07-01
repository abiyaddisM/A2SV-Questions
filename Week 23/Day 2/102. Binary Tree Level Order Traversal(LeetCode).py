# July 1 2025
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        que = deque([root])
        while que:
            size = len(que)
            temp = []
            for _ in range(size):
                pop = que.popleft()
                temp.append(pop.val)
                if pop.left:
                    que.append(pop.left)
                if pop.right:
                    que.append(pop.right)
            res.append(temp)
        return res
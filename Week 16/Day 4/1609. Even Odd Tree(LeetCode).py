# May 15 2025
# https://leetcode.com/problems/even-odd-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return

        queue = deque()
        queue.append(root)
        count = 0
        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                if i < level_size - 1:
                    nextnode = queue[0]
                    if count % 2 == 0:
                        if node.val >= nextnode.val:
                            return False
                    else:
                        if node.val <= nextnode.val:
                            return False
                if count % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                else:
                    if node.val % 2 != 0:
                        return False

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            count += 1
        return True
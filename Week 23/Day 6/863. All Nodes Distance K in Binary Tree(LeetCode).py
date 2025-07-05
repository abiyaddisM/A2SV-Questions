# July 5 2025
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        graph = defaultdict(list)

        def convert(root):
            if not root:
                return 0
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)

            convert(root.left)
            convert(root.right)

        convert(root)
        visited = set([target.val])
        level = 0
        que = deque([target.val])

        while que:
            size = len(que)
            for _ in range(size):
                curr = que.popleft()
                for ne in graph[curr]:
                    if ne not in visited:
                        que.append(ne)
                        visited.add(ne)
            level += 1
            if level == k:
                break
        return list(que)



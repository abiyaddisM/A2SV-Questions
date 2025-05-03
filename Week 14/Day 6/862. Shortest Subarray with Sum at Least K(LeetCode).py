# May 3 2025
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pre[i+1] = pre[i] + nums[i]

        que = deque()
        res = float('inf')
        for i in range(len(pre)):
            while que and pre[i] - pre[que[0]] >= k:
                res = min(res, i - que.popleft())
            while que and pre[que[-1] ] >= pre[i]:
                que.pop()
            que.append(i)
        return res if res != float('inf') else -1
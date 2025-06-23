# June 23 2025
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        pre = cardPoints[:]
        for i in range(1, len(pre)):
            pre[i] += pre[i - 1]
        res = 0
        for i in range(k + 1):
            temp = (len(cardPoints) - k) + i
            l = pre[i - 1] if i > 0 else 0
            r = pre[-1] - pre[temp - 1]
            print(l, r)
            res = max(res, l + r)
        return res
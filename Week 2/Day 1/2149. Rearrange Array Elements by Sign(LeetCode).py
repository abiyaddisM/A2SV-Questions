#February 3 2025
#https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative = []
        positive = []
        res = []
        for n in nums:
            if n > 0:
                positive.append(n)
            else:
                negative.append(n)
        for i in range(len(positive)):
            res.append(positive[i])
            res.append(negative[i])
        return res

# February 6 2025
# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        iseven = {}
        total = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                total += nums[i]
                iseven[i] = nums[i]
        res = []
        for q in queries:
            nums[q[1]] += q[0]
            if q[1] in iseven:
                total -= iseven[q[1]]
                iseven.pop(q[1])
                if nums[q[1]] % 2 == 0:
                    iseven[q[1]] = nums[q[1]]
                    total += nums[q[1]]
            else:
                if nums[q[1]] % 2 == 0:
                    iseven[q[1]] = nums[q[1]]
                    total += nums[q[1]]
            res.append(total)
        return res


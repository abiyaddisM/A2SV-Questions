# May 16 2025
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        dic = {}
        for i in range(len(temp)):
            if temp[i] not in dic:
                dic[temp[i]] = i
        res = []
        for n in nums:
            res.append(dic[n])
        return res
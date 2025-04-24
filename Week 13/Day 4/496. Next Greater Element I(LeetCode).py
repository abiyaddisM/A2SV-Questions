# April 24 2025
# https://leetcode.com/problems/next-greater-element-i/description/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for i in range(len(nums2)):
            dic[nums2[i]] = i
        stack = []
        temp = []
        nums2.reverse()
        for n in nums2:
            while stack and stack[-1] <= n:
                stack.pop()
            temp.append(stack[-1] if stack else -1)
            stack.append(n)
        temp.reverse()
        res = []
        for n in nums1:
            res.append(temp[dic[n]])
        return res
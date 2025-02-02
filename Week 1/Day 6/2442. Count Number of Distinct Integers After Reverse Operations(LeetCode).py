#Febuary 1 2025
#https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            copy = nums[i]
            count = 0
            while copy >= 1:
                copy = copy // 10
                count += 1
            copy = nums[i]
            temp = 0
            while count > 0:
                temp += (copy % 10) * (10 ** (count - 1))
                copy //= 10
                count -= 1
            nums.append(temp)
        return len(set(nums))

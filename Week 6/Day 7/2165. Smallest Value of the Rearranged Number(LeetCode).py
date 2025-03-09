# March 9 2025
# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/
class Solution:
    def smallestNumber(self, num: int) -> int:
        if -9 <= num <= 9:
            return num
        neg = num < 0
        if neg:
            num *= -1
        arr = []
        while num != 0:
            arr.append(num % 10)
            num //= 10
        if neg:
            arr.sort(reverse = True)
        else:
            arr.sort()
            a = next((i for i in range(len(arr)) if arr[i] != 0), -1)
            arr[0], arr[a] = arr[a], arr[0]
        res =  0
        for i in range(len(arr)):
            res *= 10 * min(i,1)
            res += arr[i]
        if neg:
            res *= -1
        return res
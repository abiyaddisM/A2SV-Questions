#Febuary 1 2025
#https://leetcode.com/problems/water-bottles/
class Solution:
    def numWaterBottles(self, numBot: int, numEx: int) -> int:
        count = numBot
        ex = numBot
        while ex >= numEx:
            count += ex // numEx
            ex = ex // numEx + ex % numEx
        return count

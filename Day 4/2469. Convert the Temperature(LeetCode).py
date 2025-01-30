#January 30 2025
#https://leetcode.com/problems/convert-the-temperature
class Solution:
    def convertTemperature(self, c: float) -> List[float]:
        return [c + 273.15, c * 1.80 + 32]

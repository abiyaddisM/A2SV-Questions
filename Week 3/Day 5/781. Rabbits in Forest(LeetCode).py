# February 14 2025
# leetcode.com/problems/rabbits-in-forest/description
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = Counter(answers)
        res = 0
        for k, v in dic.items():
            res += (k + 1) * (math.ceil(v / (k + 1)))
        return res
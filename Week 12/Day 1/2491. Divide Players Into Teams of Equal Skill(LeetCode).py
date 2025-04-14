# April 14 2025
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 1
        r = len(skill) - 2
        pre = skill[0] + skill[-1]
        res = skill[0] * skill[-1]
        while l < r:
            if pre != skill[l] + skill[r]:
                return -1
            res += skill[l] * skill[r]
            l += 1
            r -= 1
        return res

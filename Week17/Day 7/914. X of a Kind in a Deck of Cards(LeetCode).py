# May 25 2025
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = Counter(deck)
        minv = min(dic.values())
        for i in range(2,minv + 1):
            state = True
            for k, v in dic.items():
                if v % i != 0:
                    state = False
            if state:
                return state
        return False
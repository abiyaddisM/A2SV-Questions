# October 29 2025
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        vals = count.values()
        g = reduce(gcd, vals)
        return g >= 2
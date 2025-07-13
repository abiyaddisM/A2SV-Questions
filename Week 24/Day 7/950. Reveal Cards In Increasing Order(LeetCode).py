# July 13 2025
# https://leetcode.com/problems/reveal-cards-in-increasing-order/description/
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        nums = [0] * len(deck)
        deck.sort()
        que = deque(deck)
        nums[0] = que.popleft()
        count = 1
        i = 0
        skip = 1
        while count < len(deck):
            i = (i + 1) % len(deck)
            if nums[i] == 0 and skip:
                skip = 0
            elif nums[i] == 0:
                nums[i] = que.popleft()
                skip = 1
                count += 1
        return nums


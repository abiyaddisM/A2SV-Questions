# February 4 2025
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
class Solution:
    def matchPlayersAndTrainers(self, player: List[int], train: List[int]) -> int:
        player.sort(reverse=True)
        train.sort(reverse=True)
        count = 0
        p = 0
        t = 0
        while p < len(player) and t < len(train):
            if player[p] <= train[t]:
                t += 1
                count += 1
            p += 1
        return count
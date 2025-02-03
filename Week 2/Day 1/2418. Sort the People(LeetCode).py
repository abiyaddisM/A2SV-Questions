#February 3 2025
#https://leetcode.com/problems/sort-the-people/description/
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mydic = {}
        for i, h in enumerate(heights):
            mydic[h] = i
        heights.sort(reverse=True)
        for i in range(len(heights)):
            heights[i] = names[mydic[heights[i]]]
        return heights

# October 27 2025
# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        temp = s.split(' ')
        temp.sort(key =lambda x: x[-1])
        res = []
        for n in temp:
            res.append(n[:(len(n) -1)])
        return ' '.join(res)

#January 31 2025
#https://leetcode.com/problems/find-common-characters/
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mydic = [{} for _ in range(len(words))]
        res = []
        for i in range(len(words)):
            for w in words[i]:
                mydic[i][w] = mydic[i].get(w, 0) + 1
        temp = mydic[0]
        for t in temp:
            mins = mydic[0][t]
            for i in range(len(mydic)):
                if t not in mydic[i]:
                    mins = 0
                    break
                mins = min(mins, mydic[i][t])
            res.extend([t] * mins)

        return res

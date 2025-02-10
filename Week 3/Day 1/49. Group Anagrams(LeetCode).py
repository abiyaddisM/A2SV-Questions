# February 10 2025
# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydic = {}
        res = []

        for i in range(len(strs)):
            w = ''.join(sorted(strs[i]))
            if w in mydic:
                res[mydic[w]].append(strs[i])
            else:
                mydic[w] = len(res)
                res.append([strs[i]])

        return res
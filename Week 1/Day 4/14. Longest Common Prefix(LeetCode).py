#January 30 2025
#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minStr = min(strs,key=len)

        for i in range(len(minStr)):
            for j in range(len(strs)):
                if strs[j][i] != minStr[i]:
                    return minStr[0:i]

        return minStr
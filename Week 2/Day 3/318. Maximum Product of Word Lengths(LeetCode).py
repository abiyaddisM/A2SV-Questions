# February 5 2025
# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        myset = [set() for _ in range(len(words))]
        for i in range(len(words)):
            for j in range(len(words[i])):
                myset[i].add(words[i][j])
        maxs = 0
        print(myset[0])
        for i in range(len(myset)):
            for j in range(i + 1, len(myset)):
                for s in myset[i]:
                    if s in myset[j]:
                        break
                else:
                    maxs = max(maxs, len(words[i]) * len(words[j]))
        return maxs

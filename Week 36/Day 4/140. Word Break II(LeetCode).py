# October 2 2025
# https://leetcode.com/problems/word-break-ii/description/
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = TrieNode()

        def insert(word):
            cur = root
            for w in word:
                i = ord(w) - 97
                if not cur.children[i]:
                    cur.children[i] = TrieNode()
                cur = cur.children[i]
            cur.is_end = True

        for w in wordDict:
            insert(w)
        dic = {}

        def dp(index, word):
            if index >= len(s):
                return [word.strip()]
            res = []
            cur = root
            if (index, word) in dic:
                return dic[(index, word)]
            for i in range(index, len(s)):
                w = s[i]
                j = ord(w) - 97
                if not cur.children[j]:
                    break
                cur = cur.children[j]
                word += w
                if cur.is_end:
                    temp = dp(i + 1, word + ' ')
                    if temp:
                        res.extend(temp)
            dic[(index, word)] = res
            return res

        return dp(0, '')




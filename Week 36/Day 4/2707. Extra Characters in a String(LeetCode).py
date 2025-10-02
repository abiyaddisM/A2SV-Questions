# October 2 2025
# https://leetcode.com/problems/extra-characters-in-a-string/
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()

        def insert(word):
            cur = root
            for w in word:
                i = ord(w) - 97
                if not cur.children[i]:
                    cur.children[i] = TrieNode()
                cur = cur.children[i]
            cur.is_end = True

        for d in dictionary:
            insert(d)

        dic = {}
        def dp(index):
            if index >= len(s):
                return 0
            if index in dic:
                return dic[index]

            res = 1 + dp(index + 1)

            cur = root
            for i in range(index, len(s)):
                j = ord(s[i]) - 97
                if not cur.children[j]:
                    break
                cur = cur.children[j]
                if cur.is_end:
                    res = min(res, dp(i + 1))

            dic[index] = res
            return res

        return dp(0)

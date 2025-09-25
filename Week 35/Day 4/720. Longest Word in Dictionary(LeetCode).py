# September 25 2025
# https://leetcode.com/problems/longest-word-in-dictionary/description/
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()

        def insert(word):
            cur = root
            for w in word:
                i = ord(w) - 97
                if not cur.children[i]:
                    cur.children[i] = TrieNode()
                cur = cur.children[i]
            cur.is_end = True

        for w in words:
            insert(w)

        def helper(cur, word):
            if not cur:
                return word
            res = word
            for i in range(26):
                if cur.children[i] and cur.children[i].is_end:
                    temp = helper(cur.children[i], word + chr(97 + i))
                    res = min(res, temp) if len(temp) == len(res) else (temp if len(temp) > len(res) else res)

            return res

        return helper(root, '')
# September 26 2025
# https://leetcode.com/problems/word-break/description/
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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

        memo = {}

        def helper(word, depth):
            if word in memo:
                return memo[word]

            cur = root
            for i in range(len(word)):
                j = ord(word[i]) - 97
                if not cur.children[j]:
                    memo[word] = False
                    return False
                cur = cur.children[j]
                if cur.is_end and helper(word[i + 1:], depth + 1):
                    memo[word] = True
                    return True

            memo[word] = cur.is_end
            return memo[word]

        return helper(s, 0)

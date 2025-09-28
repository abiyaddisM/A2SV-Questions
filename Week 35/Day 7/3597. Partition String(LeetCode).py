# September 28 2025
# https://leetcode.com/problems/partition-string/description/
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
class Solution:
    def partitionString(self, s: str) -> List[str]:
        root = TrieNode()
        def insert(word):
            cur = root
            for w in word:
                i = ord(w) - 97
                if not cur.children[i]:
                    cur.children[i] = TrieNode()
                cur = cur.children[i]
            cur.is_end = True
        def search(word):
            cur = root
            for w in word:
                i = ord(w) - 97
                if not cur.children[i]:
                    return False
                cur = cur.children[i]
            return cur.is_end
        res = []
        l = 0
        while l < len(s):
            r = l + 1
            while search(s[l:r]):
                if r >= len(s):
                    break
                r += 1
            if not search(s[l:r]):
                res.append(s[l:r])
            insert(s[l:r])
            l = r


        return res
# September 24 2025
# https://leetcode.com/problems/replace-words/description/
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
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
            res = ''
            for w in word:
                i = ord(w) - 97
                if not cur.children[i]:
                    return word
                cur = cur.children[i]
                res += chr(i + 97)
                if cur.is_end:
                    return res
            return word
        for d in dictionary:
            insert(d)
        sentence = sentence.split()
        res = []
        for s in sentence:
            res.append(search(s))
        return  ' '.join(res)
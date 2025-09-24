# September 24 2025
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            i = ord(w) - 97
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.is_end = True

    def search(self, word: str) -> bool:
        return self.helper(0, word, self.root)

    def helper(self, i, word, cur):
        if i >= len(word):
            return cur.is_end
        res = False
        if word[i] == '.':
            for j in range(26):
                if cur.children[j] and self.helper(i + 1, word, cur.children[j]):
                    res = True
        else:
            j = ord(word[i]) - 97
            if cur.children[j] and self.helper(i + 1, word, cur.children[j]):
                res = True
        return res

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
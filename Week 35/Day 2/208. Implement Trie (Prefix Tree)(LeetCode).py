# September 23 2025
# https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            i = ord(w) - 97
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            i = ord(w) - 97
            if not cur.children[i]:
                return False
            cur = cur.children[i]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            i = ord(w) - 97
            if not cur.children[i]:
                return False
            cur = cur.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# September 29 2025
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()

        def insert(word):
            cur = root
            for w in word:
                if w not in cur.children:
                    cur.children[w] = TrieNode()
                cur = cur.children[w]
            cur.is_end = True
        def search(word):
            cur = root
            for w in word:
                if cur.is_end:
                    return False
                cur = cur.children[w]
            return True
        for f in folder:
            word = f.split('/')
            insert(word[1:])
        res = []
        for f in folder:
            word = f.split('/')
            if search(word[1:]):
                res.append(f)
        return res
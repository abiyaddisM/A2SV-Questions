# October 3 2025
# https://leetcode.com/problems/delete-duplicate-folders-in-system/description/
class TrieNode:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.is_end = False
        self.index = None


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode('')

        def insert(word) -> None:
            cur = root
            for w in word:
                if w not in cur.children:
                    cur.children[w] = TrieNode(w)
                cur = cur.children[w]
            cur.is_end = True

        for p in paths:
            insert(p)

        dic = defaultdict(int)

        def helper(cur):
            if not cur.children:
                sig = ()
            else:
                items = []
                for name in sorted(cur.children):
                    child = cur.children[name]
                    items.append((name, helper(child)))
                sig = tuple(items)
            cur.index = sig
            if sig:
                dic[sig] += 1
            return sig

        helper(root)

        def remove(cur) -> None:
            for name, child in list(cur.children.items()):
                if child.index and dic[child.index] > 1:
                    del cur.children[name]
                else:
                    remove(child)

        remove(root)

        res: List[List[str]] = []

        def fetch(cur, word) -> None:
            for name in sorted(cur.children):
                child = cur.children[name]
                word.append(name)
                res.append(word[:])
                fetch(child, word)
                word.pop()

        fetch(root, [])
        return res

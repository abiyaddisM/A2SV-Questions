# September 24 2025
# https://leetcode.com/problems/search-suggestions-system/description/
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]


class Solution:
    def suggestedProducts(self, products: List[str], sw: str) -> List[List[str]]:
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
                    return None
                cur = cur.children[i]
            return cur

        def prefix(word, cur, ad):
            if not cur:
                print(word)
                return []
            temp = []
            if cur.is_end:
                temp.append(ad + word)
            for i in range(26):
                if cur.children[i]:
                    t = chr(i + 97)
                    res = prefix(word + t, cur.children[i], ad)
                    if res:
                        temp.extend(res)
            return temp

        for p in products:
            insert(p)

        res = []
        for i in range(len(sw)):
            t = sw[:i + 1]
            temp = search(t)
            if not temp:
                res.append([])
                continue
            k = prefix("", temp, t)

            res.append(k[:3])
        return res
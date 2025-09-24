# September 24 2025
# https://leetcode.com/problems/map-sum-pairs/description/
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
class MapSum:

    def __init__(self):
        self.dic = defaultdict(str)
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        self.dic[key] = val
        cur = self.root
        for w in key:
            i = ord(w) - 97
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.is_end = True

    def sum(self, prefix: str) -> int:
        cur = self.root
        print(prefix)
        for w in prefix:
            i = ord(w) - 97
            print(w)
            if not cur.children[i]:
                return 0
            cur = cur.children[i]
        return self.helper(cur, '', prefix)
    def helper(self, cur, word, prefix):
        if not cur:
            return 0
        temp = 0
        if cur.is_end:
            temp += self.dic[prefix + word]
        for i in range(26):
            if cur.children[i]:
                temp += self.helper(cur.children[i], word + chr(i + 97),prefix)
        return temp


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
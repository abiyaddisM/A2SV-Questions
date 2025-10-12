# October 12 2025
# https://leetcode.com/problems/short-encoding-of-words/description/
class TrieNode:
    def __init__(self):
        self.children = [None] * 26


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))

        root = TrieNode()
        leaf_nodes = {}

        def insert_reversed(word) -> TrieNode:
            cur = root
            for ch in reversed(word):
                i = ord(ch) - 97
                if cur.children[i] is None:
                    cur.children[i] = TrieNode()
                cur = cur.children[i]
            return cur

        for w in words:
            leaf_nodes[w] = insert_reversed(w)

        def is_leaf(node):
            for child in node.children:
                if child is not None:
                    return False
            return True

        ans = 0
        for w, node in leaf_nodes.items():
            if is_leaf(node):
                ans += len(w) + 1

        return ans

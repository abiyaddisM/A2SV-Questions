# October 2 2025
# https://leetcode.com/problems/number-of-matching-subsequences/description/
from typing import List
from collections import Counter


class TrieNode:
    __slots__ = ("is_end", "end_count", "children")

    def __init__(self):
        self.is_end = False
        self.end_count = 0
        self.children = [None] * 26


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        root = TrieNode()
        buckets = [set() for _ in range(26)]

        dup = Counter(words)

        def insert(word: str, cnt: int) -> None:
            cur = root
            for idx, ch in enumerate(word):
                i = ord(ch) - 97
                if cur.children[i] is None:
                    cur.children[i] = TrieNode()
                cur = cur.children[i]
                if idx == 0:
                    buckets[i].add(cur)
            cur.is_end = True
            cur.end_count += cnt

        for w, c in dup.items():
            insert(w, c)

        res = 0

        for ch in S:
            i = ord(ch) - 97
            if not buckets[i]:
                continue
            current = list(buckets[i])
            buckets[i].clear()

            for node in current:
                if node.end_count:
                    res += node.end_count
                for nxt, child in enumerate(node.children):
                    if child:
                        buckets[nxt].add(child)

        return res

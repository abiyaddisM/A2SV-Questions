# October 25 2025
# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                index = ord(char) - ord('a')
                if node.children[index] is None:
                    node.children[index] = TrieNode()
                node = node.children[index]
                node.is_end = True

        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] != float('inf'):
                node = root
                j = i
                while j < n and node.children[ord(target[j]) - ord('a')]:
                    node = node.children[ord(target[j]) - ord('a')]
                    j += 1
                    if node.is_end:
                        dp[j] = min(dp[j], dp[i] + 1)
        return dp[n] if dp[n] != float('inf') else -1
#### May 5 2025
# https://leetcode.com/problems/k-th-symbol-in-grammar/
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 or n == 2:
            return 0 if k == 1 else 1
        size = (2 ** (n - 1)) // 2
        if k > size:
            t = k % size
            if t > (size // 2):
                k = abs(t - (size // 2))
            else:
                k = abs(t + (size // 2))
            print(k)
        return self.kthGrammar(n - 1, k)
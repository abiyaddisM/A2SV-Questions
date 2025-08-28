# August 28 2025
# https://leetcode.com/problems/satisfiability-of-equality-equations/description/
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        arr = [i for i in range(26)]

        def find(x):
            if x == arr[x]:
                return x
            return find(arr[x])

        def union(a, b):
            t1 = find(a)
            t2 = find(b)
            if t1 != t2:
                arr[t2] = t1

        for e in equations:
            if e[1] == '=':
                a = ord(e[0]) - 97
                b = ord(e[-1]) - 97
                union(a, b)
        for e in equations:
            if e[1] == '!':
                a = find(ord(e[0]) - 97)
                b = find(ord(e[-1]) - 97)
                if a == b:
                    return False

        return True

class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        res = []
        for i,n in enumerate(ast):
            if n > 0:
                res.append(n)
            else:
                while res and res[-1] > 0 and res[-1] < -n:
                    res.pop()
                if not res or res[-1] < 0:
                    res.append(n)
                elif res[-1] == -n:
                    res.pop()
        return res
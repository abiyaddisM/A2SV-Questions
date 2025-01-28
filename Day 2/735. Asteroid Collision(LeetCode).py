class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        res = []
        for a in ast:
            if a > 0:
                res.append(a)
            else:
                while res and res[-1] > 0 and res[-1] < -a:
                    res.pop()
                if not res or res[-1] < 0:
                    res.append(a)
                elif res[-1] == -a:
                    res.pop()

        return res
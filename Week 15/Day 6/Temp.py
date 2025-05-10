class Solution: def arrangeCoins(self, n: int): 
res = 0
row = 0 
while res + row + 1 <= n: 
res += 1 
row += res 
return res 

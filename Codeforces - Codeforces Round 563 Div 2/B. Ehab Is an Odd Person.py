from collections import Counter,deque
import math
def INT():
    return int(input())
def IA():
    return list(map(int,input().strip().split()))
def SA():
    return input().split()
def STR():
    return input()
def PA(arr):
    print(' '.join(map(str, arr)))
def YesNo(state):
    if state:
        print('YES')
    else:
        print('NO')


size = INT()
nums = IA()
odd = False
even = False
for n in nums:
    if n % 2 == 0:
        even = True
    else:
        odd = True
if odd and even:
    PA(sorted(nums))
else:
    PA(nums)
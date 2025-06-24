
from collections import Counter,deque, defaultdict
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
tempGraph = IA()
color = IA()
res2 = 1
for i in range(1, size):
    j = tempGraph[i - 1] - 1
    if color[j] != color[i]:
        res += 1
print(res2)



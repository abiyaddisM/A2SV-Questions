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

t = INT()
for _ in range(t):
    row, col, k = IA()
    perRow = math.ceil(k / row)
    emptySpace = col - perRow
    emptySpace += 1
    res = math.ceil(perRow / emptySpace)
    print(res)
    print(math.ceil((math.ceil(k / row)) / (col - (math.ceil(k / row)) + 1)))

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
    n, k = IA()

    def helper(k2,i):
        rem = k2 // n
        if rem == i:
            return k2
        k2 += rem - i
        return helper(k2, rem)
    print(helper(k,0 ))

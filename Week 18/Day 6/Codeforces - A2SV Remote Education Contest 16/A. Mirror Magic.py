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
    nums = STR()
    new = ''
    for n in nums:
        if n == 'p':
            new += 'q'
        elif n == 'q':
            new += 'p'
        else:
            new += 'w'
    print(new[::-1] )
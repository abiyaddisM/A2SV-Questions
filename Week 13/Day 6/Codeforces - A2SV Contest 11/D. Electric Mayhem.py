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

arr = STR()
stack = []
for a in arr:
    if stack and stack[-1] == a:
        stack.pop()
        continue
    stack.append(a)
YesNo(len(stack) == 0)
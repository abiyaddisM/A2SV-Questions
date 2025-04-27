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
for i in range(len(arr)):
    if stack and stack[-1] == arr[i]:
        stack.pop()
        continue
    stack.append(arr[i])
print(''.join(stack))
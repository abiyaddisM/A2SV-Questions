from collections import Counter, deque
import math


def INT():
    return int(input())


def IA():
    return list(map(int, input().strip().split()))


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
que = deque()
stack = []
res = ''
for a in arr:
    while que and que[-1] > a:
        que.pop()
    que.append(a)
for a in arr:
    stack.append(a)
    if a == que[0]:
        temp = que.popleft()
        while (stack and que) and stack[-1] <= que[0]:
            res += stack.pop()
print(res + ''.join(reversed(stack)))

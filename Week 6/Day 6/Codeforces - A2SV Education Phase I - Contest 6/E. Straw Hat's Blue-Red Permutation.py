from collections import Counter
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

t = INT()
for _ in range(t):
    size = INT()
    num = IA()
    color = STR()
    red = [0 for i in range(size)]
    blue = [0 for i in range(size)]
    state = True

    for i in range(size):
        if color[i] == 'R':
            if num[i] > size:
                state = False
                break
            v = max(num[i] - 1,0)
            red[v] += 1
        else:
            if num[i] < 1:
                state = False
                break
            v = min(num[i], size)
            blue[v - 1] += 1
            
    for i in range(1,size):
        blue[i] += blue[i - 1]
        red[-(i + 1)] += red[-i]

    for i in range(size):
        if size + 1 < (i + 1) + red[i]:
            state = False
            break
    for i in range(size):
        if blue[i] > i + 1:
            state = False
            break
    if state:
        print('YES')
    else:
        print('NO')




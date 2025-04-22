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
    size, k = IA()
    word = list(STR())
    count = 0
    total = 0
    temp = [0,(0,0)]
    l = 0
    for r in range(size):
        if word[r] == 'L':
            count += 1
        total += 2 if r > 0 else 1
        while count > k:
            if l > 0 and word[l - 1] == 'W':
                total -= 2
            else:
                total -= 1
            if word[l] == 'L':
                if l < size - 1:
                    total -= 1
                count -= 1
            l += 1
        if total >= temp[0]:
            temp = [total,(l,r)]
    res = 0
    for i in range(size):
        if temp[1][0] <= i <= temp[1][1]:
            word[i] = 'W'
        if i > 0 and word[i - 1] == 'W' and word[i] == 'W':
            res += 2
        elif word[i] == 'W':
            res += 1
    print(res)
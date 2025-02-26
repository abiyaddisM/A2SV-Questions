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

n, m = IA()
flag = True
for i in range(n):
        if i % 2 == 0:
            print('#' * m)
            continue

        if flag:
            print('.' * (m - 1) + '#')
        else:
            print('#' + '.' * (m - 1))

        flag = not flag
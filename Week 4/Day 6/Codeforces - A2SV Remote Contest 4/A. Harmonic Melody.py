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

n = INT()
for _ in range(n):
    size = INT()
    arr = IA()

    for i in range(size - 1):
        val =  abs(arr[i] - arr[i + 1])
        if val != 7 and val != 5:
            print('NO')
            break
    else:
        print('YES')
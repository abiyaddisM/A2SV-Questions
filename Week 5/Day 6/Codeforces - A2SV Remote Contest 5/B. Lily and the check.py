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
    x, y = IA()
    bill = 0
    count = 0
    if x > y:
        print(y)
        continue
    elif x == y:
        print(1)
        continue
    temp = x
    while temp * 10 <= y:
        temp *= 10
    while temp >= x:
        f = (y - bill) // temp
        bill += temp * f
        count += f
        temp = temp //10
    print(count + (y - bill))

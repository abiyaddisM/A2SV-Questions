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
point = IA()
cost = IA()
prize = [0,0,0,0,0]
total = 0
for i in range(t):
    total += point[i]
    for j in range(1,6):
        if total >= cost[-j]:
            prize[-j] += total // cost[-j]
            total -= cost[-j] * (total // cost[-j])
PA(prize)
print(total)
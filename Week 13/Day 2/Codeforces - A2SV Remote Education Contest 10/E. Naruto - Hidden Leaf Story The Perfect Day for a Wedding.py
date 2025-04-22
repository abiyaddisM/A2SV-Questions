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
    nums = list(STR())
    size = len(nums)
    digit = [0] * 10
    for n in nums:
        digit[int(n)] += 1
    dic = Counter(digit)
    h = max(digit)
    if dic[h] > 1:
        print(size - h * 2)
    else:
        print(size - h)
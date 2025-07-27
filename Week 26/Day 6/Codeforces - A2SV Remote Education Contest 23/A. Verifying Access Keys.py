from collections import Counter,deque, defaultdict
import heapq
import math
import sys
def INT():
    return int(sys.stdin.readline())
def IA():
    return list(map(int, sys.stdin.readline().split()))
def SA():
    return input().split()
def STR():
    return sys.stdin.readline()
def PA(arr):
    print(' '.join(map(str, arr)))
def YesNo(state):
    if state:
        print('YES')
    else:
        print('NO')

t = INT()
for _ in range(t):
    size = INT()
    arr = STR()
    state = True
    nums = []
    word = []

    if '0' <= arr[0] <= '9':
        for i in range(size):
            if '0' <= arr[i] <= '9':
                nums.append(int(arr[i]))
                continue
            word = list(arr[i:size])
            break
    else:
        word = list(arr)
        word.pop()
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            state = False
    for i in range(1, len(word)):
        if '0' <= word[i] <= '9' or word[i] < word[i - 1]:
            state = False
    YesNo(state)




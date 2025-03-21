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

size, k = IA()
nums = IA()
res = 0
maxq,minq = deque(),deque()
l = 0
for r in range(size):
    while minq and minq[-1] > nums[r]:
        minq.pop()
    minq.append(nums[r])
    while maxq and maxq[-1] < nums[r]:
        maxq.pop()
    maxq.append(nums[r])
    while maxq and minq and maxq[0] - minq[0] > k:
        if nums[l] == maxq[0]:
            maxq.popleft()
        if nums[l] == minq[0]:
            minq.popleft()
        l += 1

    res += r - l + 1
print(res)
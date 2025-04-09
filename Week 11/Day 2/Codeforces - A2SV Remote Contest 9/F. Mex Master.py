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
    size = INT()
    nums = IA()
    nums.sort()
    temp = []
    flag = False
    m = nums[0]
    freq = nums.count(m)
    if (size - freq) + 1 < freq:
        temp.append(m)
        for n in nums:
            if n != m:
                temp.append(n)
        nums = temp
        temp = []
    l = 0
    r = len(nums) - 1
    while l < r:
        temp.append(nums[l] + nums[r])
        if flag:
            r -= 1
        else:
            l += 1
        flag = not flag
    if (size - freq) + 1 < freq:
        temp.append(m + m)
    nums = sorted(temp)
    if nums[0] != 0:
        print(0)
        continue
    for i in range(len(nums) - 1):
        if nums[i] + 1 != nums[i + 1]:
            print(nums[i] + 1)
            break
    else:
        print(nums[-1] + 1)
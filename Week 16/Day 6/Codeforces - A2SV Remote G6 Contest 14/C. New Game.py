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
    def helper(card):
        queue = deque()
        queue.append(0)
        res = 1
        for r in range(1,size):
            if nums[r - 1] != nums[r]:
                if nums[r - 1] + 1 != nums[r]:
                    queue.clear()
                queue.append(r)
            while len(queue) > k:
                queue.popleft()
            res = max(res,r - queue[0] + 1)
        return res >= card

    size, k = IA()
    nums = IA()
    nums.sort()
    l = 0
    r = size
    res = 0
    while l <= r:
        m = l + (r - l) // 2
        if helper(m):
            res = m
            l = m + 1
        else:
            r = m - 1
    print(res)
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
    a = INT()
    arr = IA()
    m = INT()
    for __ in range(m):
        let = {}
        num = {}
        wom = STR()
        if len(wom) != a:
            print('NO')
            continue
        for i in range(a):
            if wom[i] in let:
                if let[wom[i]] != arr[i]:
                    print('NO')
                    break
            if arr[i] in num:
                if num[arr[i]] != wom[i]:
                    print('NO')
                    break
            let[wom[i]] = arr[i]
            num[arr[i]] = wom[i]
        else:
            print('YES')
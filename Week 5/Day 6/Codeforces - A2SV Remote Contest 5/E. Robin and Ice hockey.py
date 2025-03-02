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

t1 = STR()
t2 = STR()
t = INT()
dic1 = {}
got1 = set()
dic2 = {}
got2 = set()

for _ in range(t):
    time, team, num, card = SA()
    if team == 'h':
        if (num in dic1 and dic1[num] == 1) or card == 'r':
            if num not in got1:
                print(t1, num, time)
                got1.add(num)
        if card == 'y':
            dic1[num] = dic1.get(num,0) + 1
    else:
        if (num in dic2 and dic2[num] == 1) or card == 'r':
            if num not in got2:
                print(t2, num, time)
                got2.add(num)
        if card == 'y':
            dic2[num] = dic2.get(num,0) + 1


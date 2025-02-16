t = int(input())
num = list(map(int,input().split()))
tar = max(num) + min(num)
taken = set()
for i in range(t - 1):
    if i in taken:
        continue
    for j in range(i + 1,t):
        if num[i] + num[j] == tar and j not in taken:
            print(i + 1, j + 1)
            taken.add(j)
            break
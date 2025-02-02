n = int(input())
for _ in range(n):
    arr = list(map(int,input().split()))
    for _ in range(5):
        minIndex = arr.index(min(arr))
        arr[minIndex] += 1
    res = 1
    for a in arr:
        res *= a
    print(res)
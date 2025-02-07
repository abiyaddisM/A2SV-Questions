n = int(input())
for _ in range(n):
    size = int(input())
    arr = list(map(int,input().split()))
    count = 0
    mydic = {}
    for i in range(size):
        add = i - arr[i]
        mydic[add] = mydic.get(add,0) + 1
    for i in range(size):
        add = i - arr[i]
        if mydic[add] > 1:
            mydic[add] -= 1
            count += mydic[add]
    print(count)
n = int(input())
total = 0
for _ in range(n):
    nums = map(int,input().split())
    count = 0
    for n in nums:
        if n == 1:
            count += 1
    total += 1 if count > 1 else 0
print(total)
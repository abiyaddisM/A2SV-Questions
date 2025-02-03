n = int(input())
for _ in range(n):
    num = int(input())
    if num > 37 and ((num + 1) % 5 == 0 or (num + 2) % 5 == 0) :
        print(num + 1 if (num + 1) % 5 == 0 else num + 2)

    else:
        print(num)

n = int(input())
for _ in range(n):
    w = input()
    if len(w) >= 3 and w[0].upper() == "Y" and w[1].upper() == "E" and w[2].upper() == "S":
        print('YES')
    else:
        print('NO')
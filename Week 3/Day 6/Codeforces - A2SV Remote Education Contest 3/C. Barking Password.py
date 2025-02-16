p = input()
n = int(input())
one, two = False, False
for _ in range(n):
    k = input()
    if k[0] == p[1] or k == p:
        one = True
    if k[1] == p[0] or k == p:
        two = True
    if one and two:
        print('YES')
        break
else:
    print('NO')
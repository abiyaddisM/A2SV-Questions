n = int(input())
for _ in range(n):
    div = int(input())
    divChar = 0
    if 1900 <= div:
        divChar = 1
    elif 1600 <= div <= 1899:
        divChar = 2
    elif 1400 <= div <= 1599:
        divChar = 3
    else:
        divChar = 4
    print(f"Division {divChar}")
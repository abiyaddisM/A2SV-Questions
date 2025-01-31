#January 31 2025
#https://codeforces.com/contest/1742/my
n = int(input())
for _ in range(n):
     a, b, c = map(int, input().strip().split())
     if (a + b) == c or (a + c) == b or (b + c) == a:
         print("Yes")
     else:
         print("No")
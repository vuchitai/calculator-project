from math import sqrt
n = int(input())
sqr = int(sqrt(n))
if (sqr * sqr == n):
    print("YES")
else:
    print("NO")
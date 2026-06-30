import math

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    root = math.sqrt(total)
    if int(root + 0.5) ** 2 == total:
        print("YES")
    else:
        print("NO")
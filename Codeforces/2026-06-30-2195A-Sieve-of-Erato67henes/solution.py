import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if 67 in a:
        print("YES")
        return
    count_1 = a.count(1)
    count_7 = a.count(7)
    if count_1 > 0 and count_7 > 0:
        print("YES")
        return
    print("NO")

t = int(input())
for _ in range(t):
    solve()
import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = a[-1]
    for i in range(n-2, -1, -1):
        if a[i] > a[i+1]:
            a[i+1] += a[i]
            a[i] = 0
            a.sort()
            ans = min(ans, a[-1])
    print(ans)

t = int(input())
for _ in range(t):
    solve()
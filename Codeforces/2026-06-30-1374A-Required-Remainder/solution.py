import sys

def solve(x, y, n):
    return n - (n - y) % x

t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())
    print(solve(x, y, n))
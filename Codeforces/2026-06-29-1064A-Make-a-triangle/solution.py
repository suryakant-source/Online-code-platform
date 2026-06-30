import sys

a, b, c = map(int, input().split())
a, b, c = sorted([a, b, c])

if a + b > c:
    print(0)
else:
    print(c - a - b + 1)
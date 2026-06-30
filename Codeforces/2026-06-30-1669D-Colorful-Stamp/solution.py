import sys

def solve():
    n = int(input())
    s = input()
    s += 'W'
    n += 1
    i = 0
    while i < n:
        if s[i] == 'W':
            i += 1
            continue
        red = 0
        blue = 0
        while i < n and s[i] != 'W':
            if s[i] == 'R':
                red += 1
            else:
                blue += 1
            i += 1
        if red == 0 or blue == 0:
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    solve()
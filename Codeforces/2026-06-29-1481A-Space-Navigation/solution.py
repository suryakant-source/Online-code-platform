import sys

def solve(px, py, s):
    x, y = 0, 0
    for c in s:
        if c == 'U':
            y += 1
        elif c == 'D':
            y -= 1
        elif c == 'R':
            x += 1
        elif c == 'L':
            x -= 1

    if x == px and y == py:
        return "YES"

    if px >= 0 and py >= 0:
        count_r = s.count('R')
        count_u = s.count('U')
        if count_r >= px and count_u >= py:
            return "YES"
    elif px <= 0 and py <= 0:
        count_l = s.count('L')
        count_d = s.count('D')
        if count_l >= -px and count_d >= -py:
            return "YES"
    elif px >= 0 and py <= 0:
        count_r = s.count('R')
        count_d = s.count('D')
        if count_r >= px and count_d >= -py:
            return "YES"
    elif px <= 0 and py >= 0:
        count_l = s.count('L')
        count_u = s.count('U')
        if count_l >= -px and count_u >= py:
            return "YES"

    return "NO"

t = int(input())
for _ in range(t):
    px, py = map(int, input().split())
    s = input()
    print(solve(px, py, s))
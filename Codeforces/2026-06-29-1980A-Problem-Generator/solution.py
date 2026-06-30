import sys

def solve():
    n, m = map(int, input().split())
    a = input()
    count = [0] * 7
    for char in a:
        count[ord(char) - ord('A')] += 1
    ans = 0
    for i in range(7):
        if count[i] == 0:
            ans += 1
    print(max(0, ans - (7 - m)))

t = int(input())
for _ in range(t):
    solve()
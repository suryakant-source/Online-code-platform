import sys

def solve():
    k = int(input())
    n = 0
    while True:
        n += 1
        count = 0
        for i in range(1, n + 1):
            odd = 0
            for j in range(1, n + 1):
                if i % j == 0:
                    odd += 1
            if odd % 2 == 1:
                count += 1
        if count == k:
            print(n)
            return

t = int(input())
for _ in range(t):
    solve()
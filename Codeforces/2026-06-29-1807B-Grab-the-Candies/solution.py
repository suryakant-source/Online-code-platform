import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    even_sum = sum(x for x in a if x % 2 == 0)
    odd_sum = sum(x for x in a if x % 2 != 0)
    print("YES" if even_sum > odd_sum else "NO")

t = int(input())
for _ in range(t):
    solve()
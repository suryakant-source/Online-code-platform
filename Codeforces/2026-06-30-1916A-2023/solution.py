import sys

def solve():
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    product = 1
    for num in b:
        product *= num
    if 2023 % product != 0:
        print("NO")
        return
    print("YES")
    print(2023 // product, end=" ")
    for _ in range(k - 1):
        print(1, end=" ")
    print()

t = int(input())
for _ in range(t):
    solve()
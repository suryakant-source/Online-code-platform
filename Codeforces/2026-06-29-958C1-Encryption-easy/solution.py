import sys

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))

    total_sum = sum(a) % p
    max_sum = 0
    current_sum = 0

    for i in range(n - 1):
        current_sum = (current_sum + a[i]) % p
        max_sum = max(max_sum, (current_sum + (total_sum - current_sum)) % p)

    print(max_sum)

if __name__ == "__main__":
    main()
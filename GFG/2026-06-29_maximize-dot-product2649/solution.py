class Solution:
    def maxDotProduct(self, a, b):
        n, m = len(a), len(b)
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == n or j == m:
                return 0
            ans = max(dp(i + 1, j), a[i] * b[j] + dp(i + 1, j + 1), dp(i, j + 1))
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
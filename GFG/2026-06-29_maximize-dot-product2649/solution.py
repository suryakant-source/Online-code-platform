class Solution:
    def maxDotProduct(self, a: list[int], b: list[int]) -> int:
        m, n = len(a), len(b)
        memo = {}
        def dp(i, j):
            if i == m or j == n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            ans = max(a[i]*b[j] + dp(i+1, j+1), dp(i+1, j), dp(i, j+1))
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)
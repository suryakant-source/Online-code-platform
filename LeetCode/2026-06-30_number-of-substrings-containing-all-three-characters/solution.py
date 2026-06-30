class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def is_valid(substring):
            return 'a' in substring and 'b' in substring and 'c' in substring

        count = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if is_valid(s[i:j]):
                    count += 1
        return count
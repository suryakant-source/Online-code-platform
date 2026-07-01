class Solution:
    def maxSumSubarray(self, arr):
        n = len(arr)
        max_sum = float('-inf')
        max_sum_skipped = float('-inf')
        
        current_sum = 0
        current_sum_skipped = 0
        
        for i in range(n):
            current_sum = max(arr[i], current_sum + arr[i])
            max_sum = max(max_sum, current_sum)
            
            if i > 0:
                current_sum_skipped = max(arr[i], current_sum_skipped + arr[i])
                max_sum_skipped = max(max_sum_skipped, current_sum_skipped)
                
                current_sum_skipped = max(current_sum_skipped, current_sum)
                max_sum_skipped = max(max_sum_skipped, current_sum)
        
        return max(max_sum, max_sum_skipped)
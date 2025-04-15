class Solution:

    def findMaxAverage(self, nums, k):
        n = len(nums)
        curr_sum = 0

        # Base case to find average for first window 
        for i in range(k):
            curr_sum += nums[i]

        max_avg = curr_sum / k  

        # NOw find for remaining windows
        for i in range(k, n):

            curr_sum += nums[i]
            # this substraction is for previous window element
            curr_sum -= nums[i-k]
            avg = curr_sum / k
            # Finding maximum average
            max_avg = max(max_avg, avg)

        return max_avg  

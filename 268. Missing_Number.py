class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        total_sum = (n*(n+1)) // 2
        actual_sum = sum(nums)

        return total_sum -actual_sum

# The approach is that forst we sum the array uptill n, then sum the given array,  then we take a diffference of both of them to get the actual answer.  

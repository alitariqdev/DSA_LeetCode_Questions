class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Approach
          
        # n = len(nums) T.C -->  O(n^2), 

        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # Optimized Approach -> O(N)
        # Create a map,, and on each iteration, subtract the target from current element and check that current element is lready in the map or not... 
        # then if its there return the current element index and that element index
        n = len(nums)
        my_map = {}
        for i in range(n):
            element = target - nums[i]
            if element in my_map:
                return [i, my_map[element]]

            my_map[nums[i]] = i 

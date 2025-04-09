class Solution:
    # BRUTE-FORCE APPROACH 
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            count = 0 
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            res.append(count)
        return res






    # OPTIMIZED APPROACH 
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # Sort The Array 
        sorted_nums = sorted(nums)
        
        num_to_count = {}

        i = 0
        while i < len(sorted_nums):
            num = sorted_nums[i]
            # Insert only if the element is unique and doesnt exist in dictionary
            if num not in num_to_count:
                num_to_count[num] = i
            i += 1
        

        # Construct Resultant Array
        result = []
        for num in nums:
            result.append(num_to_count[num])
        
        return result




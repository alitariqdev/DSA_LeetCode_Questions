class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        h_set = set()

        for num in nums:
            h_set.add(num)

        if len(nums) == len(h_set):
            return False
        
        return True
        

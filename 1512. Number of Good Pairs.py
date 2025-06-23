class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_of_good_pairs = 0
        count = {}


        for i in range(len(nums)):
            count_of_good_pairs += count.get(i,0)
            count[i] = count.get(i,0) + 1 

        return count_of_good_pairs



        

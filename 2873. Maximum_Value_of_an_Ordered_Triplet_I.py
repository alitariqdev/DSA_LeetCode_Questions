# from itertools import combinations
# class Solution:
#     def maximumTripletValue(self, nums: List[int]) -> int:
        
#         n = len(nums)

#         triplets = list(combinations(nums, 3))
#         p,j,k = 0,1,2
#         print(triplets)
#         max_triplet = 0 
#         for i in range(len(triplets)):

#             value = triplets[i]
#             triplet_value = (value[p]- value[j]) * value[k]

#             if triplet_value > max_triplet:
#                 max_triplet = triplet_value

#         return max_triplet


from itertools import combinations
from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_triplet = 0
        
        for a, b, c in combinations(nums, 3):  # Correctly unpack triplet
            triplet_value = (a - b) * c  # Apply formula correctly
            
            max_triplet = max(max_triplet, triplet_value)
        
        return max_triplet

# The first one is iterative (brute force approach), we generate power set, on the basis of last generated values
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      outer = [[]]
      for num in nums:
          n = len(outer)
        for i in range(n):
						internal = outer[i] + [num]
					  outer.append(internal)
			return outer
          
  

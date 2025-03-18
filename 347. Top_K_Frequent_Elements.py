class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    #  Step # 1 Count frequencies
    freq_map = {}
    for num in nums:
      if num in freq_map:
        freq_map[num] += 1
      else:
        freq_map[num] = 1
        
    #  Step # 2 Sort the frequency mapping list
    freq_list = sorted (freq_map.items(), key=lambda x: x[1], reverse = True)
    
    #  Step # 3 GET Top k frequent elements
    top_k = [item[0] for item in freq_list[:k]]

    return top_k

    
    
    

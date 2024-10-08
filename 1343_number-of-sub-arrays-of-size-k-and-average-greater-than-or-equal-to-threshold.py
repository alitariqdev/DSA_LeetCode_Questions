from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0 
        curr_sum = sum(arr[:k-1])
        for l in range(len(arr) - k + 1):
            curr_sum += arr[l + k - 1]
            if(curr_sum/k) >= threshold:
                count += 1
            curr_sum -= arr[l]
        return count


        
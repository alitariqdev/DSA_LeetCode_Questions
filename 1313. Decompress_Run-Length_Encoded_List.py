from typing import List
def decompressRLElist(nums: List[int]) -> List[int]:

    result = []

    for i in range(0, len(nums), 2):
        result.extend([nums[i+1]]*nums[i])
    return result
    


nums = [1,2,3,4]
print(decompressRLElist(nums))
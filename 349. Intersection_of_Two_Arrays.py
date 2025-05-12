class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        arr = [] 
        set_nums1 = set(nums1)

        for i in range(len(nums2)):
            if nums2[i] in set_nums1 and nums2[i] not in arr:
                arr.append(nums2[i])
            
        return arr








# second solution


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        a = set(nums1)
        b = set(nums2)
        for i in a:
            if i in b:
                res.append(i)
        return res

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        # Traverse nums2 from right to left
        for num in reversed(nums2):
            # Pop elements smaller than current num
            while stack and stack[-1] <= num:
                stack.pop()
            # The next greater element is the top of the stack if it exists
            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1
            # Push current num onto the stack
            stack.append(num)
        
        # Build the result for nums1
        result = []
        for num in nums1:
            result.append(next_greater[num])
        
        return result

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        n = len(nums)
        curr = []
        used = [False] * n 
        output = []
        def dfs():
            if len(curr) == n:
                output.append(curr.copy())
                return


            for i in range(n):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                curr.append(nums[i])
                dfs()
                
                used[i] = False
                curr.pop()
                
        dfs()
        return output 


        
        

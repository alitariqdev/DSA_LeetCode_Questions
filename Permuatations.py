class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        curr = []
        used = [False] * n 
        output = []
        def dfs():
            if len(curr) == n:
                output.append(curr.copy())
                return


            for i in range(n):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    dfs()
                    
                    used[i] = False
                    curr.pop()
                
        dfs()
        return output 


        
        

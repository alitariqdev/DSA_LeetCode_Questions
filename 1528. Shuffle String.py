class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Create an empty array of length string
        result = [""] * len(s)
        # loop thorigh the indices array and place the cvharacetr one by one in the result array
        for i in range(len(indices)):
            result[indices[i]] = s[i]
        # Redturn the array by joining it at the end
        return "".join(result)  
        

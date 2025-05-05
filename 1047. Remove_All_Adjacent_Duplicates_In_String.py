class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []
        res_str = ""


        for char in s:
            if len(stack) > 0  and stack[-1] == char:
                stack.pop() 
            else:
                stack.append(char)

        for i in range(len(stack)):
            res_str += stack[i]

        return res_str
        

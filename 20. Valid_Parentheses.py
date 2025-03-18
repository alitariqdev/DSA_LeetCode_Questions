class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {

            ")" : "(",
            "}" : "{",
            "]" : "["

        }
        
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            
            elif stack and stack[-1] == mapping[ch]:
                stack.pop()
            else:
                return False

        return True if not stack else False
        # Return statement is checking wether if all brackets are matched or not. If there are opening brackets left in the stack, it means all the brackets are not correctly matched so return False, if all the brackrts
        # are correctly matched, the stack would be empty and it willl return True.
            

        

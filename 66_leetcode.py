# My Solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        number_str = ""
        result= []

        for i in range(0, len(digits)):
            number_str += str(digits[i])

        number_int = int(number_str) + 1
        number_str = str(number_int)
        
        for i in number_str:
            result.append(int(i))
       
        return result
    
# Second solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits # For edge case: 9, 999, we add 1 in the inital and return, this statement will merge two lists. 

      

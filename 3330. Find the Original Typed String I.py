class Solution:
    def possibleStringCount(self, word: str) -> int:

        n = len(word)
        count = 0

        for i in range(1,n):
            if word[i] == word[i-1]:
                count += 1
        
        return count + 1



# we start checking from index 1 , if its dup;ictae, it moght have typed it mistakenly (i.e. pressed for too long) just chech the previous and , if its same, in
# crement the count . At th end (+1) is for whole string, may be no character was pressed mistakenly, all the string was intended as it is. 

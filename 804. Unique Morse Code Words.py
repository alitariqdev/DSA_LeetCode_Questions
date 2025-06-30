class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..", "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()

        for word in words:
            morse_word = "".join(morse_codes[ord(char) - ord('a')] for char in word)
            seen.add(morse_word)

        return len(seen)

        
        

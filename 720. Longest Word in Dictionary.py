from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Step 1: Sort the words alphabetically
        # This ensures that we process smaller and lexicographically earlier words first
        words.sort()

        # Step 2: Create a set to keep track of valid words that can be built step-by-step
        # Start by adding an empty string to the set because it's the base for all words
        words_set = set()
        words_set.add("")

        # Step 3: This will store the final answer (the longest valid word)
        longest_word = ""

        # Step 4: Go through each word in the sorted list
        for word in words:
            # Step 5: Check if the word can be built from previous valid word
            # word[:-1] means the word without its last character
            if word[:-1] in words_set:
                # Step 6: Since it's valid, add the word to the set
                words_set.add(word)

                # Step 7: If this word is longer than the previously found one, update it
                # If same length, lexicographical order is already handled by sorting
                if len(word) > len(longest_word):
                    longest_word = word

        # Step 8: Return the longest valid word found
        return longest_word

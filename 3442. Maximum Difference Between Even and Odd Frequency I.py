class Solution:
    def maxDifference(self, s: str) -> int:
        my_map = {}
        for char in s:
            my_map[char] = my_map.get(char, 0) + 1

        odd_freqs = []
        even_freqs = []

        for count in my_map.values():
            if count % 2 == 0:
                even_freqs.append(count)
            else:
                odd_freqs.append(count)

        if not odd_freqs or not even_freqs:
            return -1

        return max(odd_freqs) - min(even_freqs)

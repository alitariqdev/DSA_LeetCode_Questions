class Solution:
    def numSplits(self, s: str) -> int:

        n = len(s)
        prefix = [0] * n  
        suffix = [0] * n

        pre_set, suf_set= set(), set()
        # calculate unique characters count from left to right (prerfix)
        for i in range(n):
            pre_set.add(s[i])
            prefix[i] = len(pre_set)

              # Calculate unique character counts from right to left (suffix)
        for i in range(n - 1, -1, -1):
            suf_set.add(s[i])
            suffix[i] = len(suf_set)

        # Count the number of good splits
        good_ways = 0
        for i in range(1, n):  # Start from 1 to split at valid positions
            if prefix[i - 1] == suffix[i]:
                good_ways += 1

        return good_ways
        

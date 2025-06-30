class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            lsb = n & 1
            reverseLsb = lsb << (31 - i)
            result = result | reverseLsb
            n = n >> 1
        return result

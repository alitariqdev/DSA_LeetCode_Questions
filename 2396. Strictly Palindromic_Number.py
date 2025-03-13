class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def check_palindrome(s: str) -> bool:
            return s == s[::-1]

        def to_base(n: int, base: int) -> str:
            ans = ""
            while n > 0:
                ans = str(n % base) + ans
                n //= base
            return ans
        
        for base in range(2, n - 1):
            if not check_palindrome(to_base(n, base)):
                return False
            else:
                continue

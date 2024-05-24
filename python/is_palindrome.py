# First attempt

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
# Slightly Optimized 

    def is_palindrome(x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]
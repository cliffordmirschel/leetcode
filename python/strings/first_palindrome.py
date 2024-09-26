class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        def is_palindrome(x):
            return x == x[::-1]
        for word in words:
            if is_palindrome(word):
                return word
        return ""
        
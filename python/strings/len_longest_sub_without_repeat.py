"""

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 s

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

# First solution works, too slow
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a variable to store the longest len of sub strings
        def no_repeats(text):
                return len(set(text)) == len(text)
        res = 0

        # Iterate through the string getting every substring
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if  no_repeats(s[i:j+1]):
                     res = max(res, len(s[i:j+1]))
        
                
        

        # return longest substirng len
        return res

def lengthOfLongestSubstring(s: str) -> int:
        start = 0  # This marks the beginning of our current substring
        end = 0    # This marks the end of our current substring
        max_len = 0  # This will keep track of the longest substring we've found so far
        char_index = {}  # This is like a dictionary where we store the last position we saw a character

        # We'll go through each character in the string, one by one
        for end in range(len(s)):  
            # If we've seen this character before AND it's within our current substring...
            if s[end] in char_index and char_index[s[end]] >= start:  
                # ...we need to move the start of our substring to just after the previous occurrence of this character
                start = char_index[s[end]] + 1  
            # We update the last seen position of this character in our dictionary
            char_index[s[end]] = end 
            # We check if our current substring is longer than the longest one we've found so far
            max_len = max(max_len, end - start + 1)  

        # After checking all characters, we return the length of the longest substring
        return max_len
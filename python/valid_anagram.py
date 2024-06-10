from collections import Counter
# First attempt
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)

        for char in t_count:
            if char not in s_count or s_count[char] != t_count[char]:
                return False

        for char in s_count:
            if char not in t_count or s_count[char] != t_count[char]:
                return False 
        return True
    
# Optimized Solution

def is_anagram(s: str, t: str):
    return Counter(s) == Counter(t)
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)
        for letter in t_count:
            if letter not in s_count or t_count[letter] > s_count[letter]:
                return letter
            
            
# Optimized Solution

class Solution:
    def find_the_difference(self, s: str, t: str) -> str:
        for i in t:
            if s.count(i) != t.count(i):
                return i

        
       
                
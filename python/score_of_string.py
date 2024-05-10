class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum([abs(ord(s[i+1]) - ord(s[i])) for i in range(len(s)-1)])
    

def score__of_string( s: str) -> int:
    res=0
    for i in range(1,len(s)):
        res+=abs(ord(s[i])-ord(s[i-1]))
    return res 
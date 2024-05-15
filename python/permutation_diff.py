class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        for i, v in enumerate(s):
            ans += abs(i-t.index(v))
        return ans
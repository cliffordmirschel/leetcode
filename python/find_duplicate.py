from collections import Counter

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res = []
        counts = Counter(nums)
        for count in counts:
            item = counts[count]
            if item > 1:
                res.append(count)
        return res


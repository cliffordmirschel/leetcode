from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words_1 = s1.split()
        words_2 = s2.split()
        s1_count = Counter(words_1)
        s2_count = Counter(words_2)
        res = []
        for item in s1_count:
            if item not in s2_count and s1_count[item] == 1:
                res.append(item)
        for item in s2_count:
            if item not in s1_count and s2_count[item] == 1:
                res.append(item)
            


        return res
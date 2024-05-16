class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        res = []
        for idx,val in enumerate(words):
            if x in val:
                res.append(idx)
        return res
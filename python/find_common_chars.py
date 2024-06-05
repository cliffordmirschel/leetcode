class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        chars = set(words[0])
        res = []

        for ch in chars: 
            freq = min([word.count(ch) for word in words])
            res += ch * freq
        return res
class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_word_count = 0

        for sentence in sentences:
            res = sentence.split()
            max_word_count = max(len(res), max_word_count)

        return max_word_count
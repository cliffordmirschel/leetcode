class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        count = 0 
        print(expected)
        two = zip(heights, expected)
        for item in two:
            if item[0] != item[1]:
                count += 1
        return count
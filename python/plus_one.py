class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Converting integer list to string list
        s = [str(i) for i in digits]
        
        # Join list items using join()
        res = int("".join(s))
        # Increment the number by 1
        res += 1
        ans = list(map(int, str(res)))
        return ans

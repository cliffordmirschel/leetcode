import functools
class Solution:
    def arraySign(self, nums: list[int]) -> int:
        def signFunc(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0
        res = functools.reduce((lambda x, y: x * y), nums)
        return signFunc(res)
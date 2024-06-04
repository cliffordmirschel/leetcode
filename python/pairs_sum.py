class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        res = 0

        for idx, val in enumerate(nums):
            for i in range(idx + 1,len(nums)):
                if val + nums[i] < target:
                    res += 1
        return res
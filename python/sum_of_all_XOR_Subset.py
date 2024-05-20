class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res |= num
        return res * (1 << (len(nums) - 1))
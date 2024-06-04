class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            res.append(curr_sum)

        return res
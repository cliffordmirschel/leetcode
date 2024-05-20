class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        new_nums = []
        for i in range(n):
            new_nums.append(nums[i])
            new_nums.append(nums[i+n])
        return new_nums
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            comp = target - val
            if comp in hashmap:
                return [hashmap[comp], i]
            if val not in hashmap:
                hashmap[val] = i
        return
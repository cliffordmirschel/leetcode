# Initial solution

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)

        
        return False
    
# Optimized solution

def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums)!=len(set(nums))
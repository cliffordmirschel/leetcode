class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        count = 0
        for num in hours:
            if num >= target:
                count += 1
        return count
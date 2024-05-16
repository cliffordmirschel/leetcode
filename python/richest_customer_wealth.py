class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        rich = 0
        for account in accounts:
            acc_sum = sum(account)
            rich = max(rich, acc_sum)

        return rich
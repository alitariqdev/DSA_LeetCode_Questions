class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest_customer = 0
        for i in range(len(accounts)):
            total_wealth = sum(accounts[i])
            richest_customer= max(richest_customer, total_wealth)
        return richest_customer




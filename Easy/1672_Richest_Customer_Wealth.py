class Solution(object):
    def maximumWealth(self, accounts):
        """
        You are given an m x n integer grid accounts where accounts[i][j] is
        the amount of money the ith customer has in the jth bank.
        Return the wealth that the richest customer has.

        A customer's wealth is the amount of money they have in all their bank accounts.
         The richest customer is the customer that has the maximum wealth.

        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0
        current = 0
        for x in accounts:
            for y in x:
                current = current + y
            if current > richest:
                richest = current
            current = 0
        return richest

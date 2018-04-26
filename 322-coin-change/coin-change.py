# -*- coding:utf-8 -*-


#
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
#
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
#
#
# Example 2:
# coins = [2], amount = 3
# return -1.
#
#
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def coinChange1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #DP
        INF = 0x7fffffff  # Using float("inf") would be slower.
        amounts = [INF] * (amount + 1)
        amounts[0] = 0
        for i in xrange(amount + 1):
            if amounts[i] != INF:
                for coin in coins:
                    if i + coin <= amount:
                        amounts[i + coin] = min(amounts[i + coin], amounts[i] + 1)
        return amounts[amount] if amounts[amount] != INF else -1
    #DFS
    def coinChange(self, coins, amount):    
        coins.sort(reverse = True)
        maxx = amount / coins[-1] + 1
        n, self.res = len(coins), maxx # 2**31-1

        def dfs(idx, rem, count):
            if rem == 0:
                self.res = min(self.res, count)
                return
            for i in range(idx, n):
                if coins[i] <= rem < coins[i] * (self.res-count): # if hope still exists
                    dfs(i, rem-coins[i], count+1)

        dfs(0, amount, 0)    
        return self.res if self.res < maxx else -1 

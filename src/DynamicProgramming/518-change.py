class Solution(object):
    def change(self, amount, coins):
        """
        给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
        
        请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
        假设每一种面额的硬币有无限个。
        题目数据保证结果符合 32 位带符号整数。
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # f[i][j] = f[i-1][j] + f[i][j-w]
        n = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount+1):
                if j == 0:
                    dp[j] = 1
                    continue
                dp[j] += dp[j-coin]
        
        return dp[amount]
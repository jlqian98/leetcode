class Solution(object):
    def integerBreak(self, n):
        """
        给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
        返回 你可以获得的最大乘积 。
        :type n: int
        :rtype: int
        """

        # f[i] = max(f[i-j]*j, (i-j)*j), j = 1, 2, ..., i-1

        if n == 2:
            return 1

        dp = [0 for i in range(n+1)]
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1]
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j]*j, (i-j)*j)
        
        return dp[n]
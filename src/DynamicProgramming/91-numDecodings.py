class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n+1)

        for i in range(n+1):
            if i <= 1:
                dp[i] = 1
                continue
            dp[i] = 0
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i >= 2 and 10 <= int(s[i-2: i]) <= 26:
                dp[i] += dp[i-2]

        return dp[n]
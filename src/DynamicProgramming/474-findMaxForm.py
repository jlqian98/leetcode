class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

        请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
        如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        length = len(strs)
        
        dp = [[[0] * (m+1) for _ in range(n+1)] for _ in range(length+1)]
        sum_0 = [sum([c=='0' for c in strs[idx]]) for idx in range(length)]
        sum_1 = [sum([c=='1' for c in strs[idx]]) for idx in range(length)]

        for i in range(length+1):
            for j in range(n+1):
                for k in range(m+1):
                    if i == 0:
                        dp[i][j][k] = 0
                        continue
                    dp[i][j][k] = dp[i-1][j][k]
                    if sum_0[i-1] <= k and sum_1[i-1] <= j:
                        dp[i][j][k] = max(dp[i-1][j-sum_1[i-1]][k-sum_0[i-1]] + 1, dp[i][j][k])
                        

        return dp[length][n][m]
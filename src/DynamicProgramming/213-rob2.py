class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        n = len(nums)
        
        dp = [[0, 0] for _ in range(n)]     # 第i个为止能拿到的最大金额，第一维代表拿第一个房子的情况，第二维代表不拿第一个房子的情况
        
        for i in range(n):
            if i == 0:
                dp[i][0] = nums[0]  # 拿第一个房子
                dp[i][1] = 0        # 不拿第一个房子
            elif i == 1:
                dp[i][0] = nums[0]
                dp[i][1] = nums[1]
            elif i == n-1:
                dp[i][0] = dp[i-1][0]   # 不能拿最后一个房子
                dp[i][1] = max(dp[i-1][1], dp[i-2][1]+nums[i])
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-2][0]+nums[i])
                dp[i][1] = max(dp[i-1][1], dp[i-2][1]+nums[i])
        
        return max(dp[n-1][0], dp[n-1][1])
        
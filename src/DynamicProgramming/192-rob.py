class Solution(object):
    def rob(self, nums):
        """
        你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
        给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)

        dp = [0] * (n)

        for idx in range(0, n):
            if idx == 0:
                dp[idx] = nums[idx]
            elif idx == 1:
                dp[idx] = max(nums[0], nums[1])
            else:
                dp[idx] = max(dp[idx-1], dp[idx-2] + nums[idx])
        
        return dp[n-1]
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

        例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
        给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

        子数组 是数组中的一个连续序列。
        :type nums: List[int]
        :rtype: int
        """
        # 1, 3, 5, 7, 9, 11 (5-0-1)
        if len(nums) <= 2:
            return 0
        
        n = len(nums)
        dp = [[0, 0] for _ in  range(n)]

        for i in range(n):
            if i <= 1:
                dp[i][0] = 0
                dp[i][1] = 0
                continue
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i][0] = dp[i-1][0] + (i - dp[i-1][1]-1)
                dp[i][1] = dp[i-1][1]
            else:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = i-1

        return dp[n-1][0]
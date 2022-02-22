class Solution(object):
    def canPartition(self, nums):
        """
        给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
        :type nums: List[int]
        :rtype: bool
        """
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        target = sum_nums // 2

        n = len(nums)
        dp = [False] * (target + 1)

        for i in range(n+1):
            for j in range(target, -1, -1):
                if j == 0:
                    dp[j]= True
                    continue
                if j >= nums[i-1]:
                    dp[j] = dp[j] or dp[j-nums[i-1]]
                else:
                    dp[j] = dp[j]
        
        return dp[target]
        

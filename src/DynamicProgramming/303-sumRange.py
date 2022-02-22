class NumArray(object):
    
    def __init__(self, nums):
        """
        给定一个整数数组  nums，处理以下类型的多个查询:

        计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
        实现 NumArray 类：

        NumArray(int[] nums) 使用数组 nums 初始化对象
        int sumRange(int i, int j) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )

        :type nums: List[int]
        """
        self.nums = nums
        sum = 0
        self.dp = [0] * (len(nums))
        for i in range(len(nums)):
            sum += nums[i]
            self.dp[i] = sum


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        
        if left == 0:
            return self.dp[right]
        else:
            return self.dp[right] - self.dp[left-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
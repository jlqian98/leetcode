class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。

        请你找出并返回只出现一次的那个数。
        你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums)

        while left < right:
            mid = (left + right ) // 2
            flag = nums[mid] == nums[mid-1]
            if (flag and mid % 2 == 1) or ((not flag) and mid % 2 == 0):
                left = mid + 1
            else:
                right = mid
        
        return nums[left-1]
                
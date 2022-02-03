class Solution(object):
    def searchRange(self, nums, target):
        """
        给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
        如果数组中不存在目标值 target，返回 [-1, -1]。
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = -1, len(nums)-1

        # 找第一个比target小的
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid
        ans_0 = left + 1
        
        # 找第一个比target大的
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        ans_1 = right - 1

        if ans_0 > ans_1:
            return [-1, -1]

        return [ans_0, ans_1]

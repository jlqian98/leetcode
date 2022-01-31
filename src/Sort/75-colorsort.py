class Solution(object):
    def sortColors(self, nums):
        """
        给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
        我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(x, a, b):
            t = x[a]
            x[a] = x[b]
            x[b] = t

        p0, p2 = 0, len(nums)-1
        for i in range(len(nums)):
            if nums[i] == 0:
                swap(nums, i, p0)
                p0 += 1
        for i in range(len(nums)-1, p0-1, -1):
            if nums[i] == 2:
                swap(nums, i, p2)
                p2 -= 1

            
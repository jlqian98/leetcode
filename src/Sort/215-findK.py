"""
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/shu-zu-zhong-de-di-kge-zui-da-yuan-su-li-ajvg/
"""
# 快速排序
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
        请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, left, right):
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] <= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] >= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            return left
        
        def quick_sort(nums, left, right):
            if left < right:
                pos = partition(nums, left, right)
                quick_sort(nums, left, pos - 1)
                quick_sort(nums, pos + 1, right)
        
        quick_sort(nums, 0, len(nums)-1)
        return nums[k-1]

# 快速排序分治思想
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def find(nums, left, right):
            pivot = nums[left]
            temp_left = left
            temp_right = right
            while left < right:
                while left < right and nums[right] <= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] >= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot

            if left == k-1:
                return nums[left]
            elif left < k-1:
                return find(nums, left + 1, temp_right)
            else:
                return find(nums, temp_left, left - 1)
            
        return find(nums, 0, len(nums)-1)

        
        
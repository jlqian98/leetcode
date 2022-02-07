class Solution(object):
    def trap(self, height):
        """
        给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        max_l, max_r = height[0], height[-1]
        ans = 0
        while left < right:
            if max_l < max_r:
                ans += max_l - height[left] 
                left += 1
                max_l = height[left] if height[left] > max_l else max_l 
            else:
                ans += max_r - height[right]
                right -= 1
                max_r = height[right] if height[right] > max_r else max_r
        return ans
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
        注意:

        可以认为区间的终点总是大于它的起点。
        区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x[1])
        ans = 1
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                ans += 1
                end = intervals[i][1]
        return len(intervals) - ans
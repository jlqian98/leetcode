class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        给你一个大小为 m x n 的二进制矩阵 grid 。

        岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
        岛屿的面积是岛上值为 1 的单元格的数目。
        计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
        :type grid: List[List[int]]
        :rtype: int
        """
        long, high = len(grid[0]), len(grid)
        visited = [[0]*51 for _ in range(51)]

        self.area = 0
        def dfs(m, n):
            if m < 0 or n < 0 or m >= high or n >= long or grid[m][n] == 0 or visited[m][n]:
                return
            visited[m][n] = 1
            self.area += 1
            for i, j in [(0,1), (0,-1), (1,0), (-1,0)]:
                dfs(m+i, n+j)
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.area = 0
                dfs(i, j)
                max_area = max(self.area, max_area)
        
        return max_area



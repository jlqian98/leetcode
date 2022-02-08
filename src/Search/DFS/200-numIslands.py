class Solution(object):
    def dfs(self, m, n, x, y, grid):
        if m < 0 or n < 0 or m == x or n == y or grid[m][n] == '0':
            return
        grid[m][n] = '0'
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self.dfs(m+i, n+j, x, y, grid)

    def numIslands(self, grid):
        """
        给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

        岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
        此外，你可以假设该网格的四条边均被水包围。
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        x = len(grid)
        y = len(grid[0])
        for m in range(x):
            for n in range(y):
                if grid[m][n] == '1':
                    ans += 1
                    self.dfs(m, n, x, y, grid)
        return ans
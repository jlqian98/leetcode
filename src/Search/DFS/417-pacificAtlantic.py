class Solution(object):
    def pacificAtlantic(self, heights):
        """
        给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。

        规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。
        请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        def inX(m, n, x, y):
            return 0 <= m < x and 0 <= n < y

        def Pacisic(grid, m, n, x, y, visited):
            if m < 0 or n < 0:
                return True
            if m == x or n == y:
                return False
            visited[m][n] = 1
            ans = False
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not inX(m+i, n+j, x, y):
                    ans = ans or Pacisic(grid, m+i, n+j, x, y, visited)
                else:
                    if not visited[m+i][n+j] and grid[m][n] >= grid[m+i][n+j]:
                        ans = ans or Pacisic(grid, m+i, n+j, x, y, visited)
            return ans
        
        def Atlantic(grid, m, n, x, y, visited):
            if m < 0 or n < 0:
                return False
            if m == x or n == y:
                return True
            visited[m][n] = 1
            ans = False
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not inX(m+i, n+j, x, y):
                    ans = ans or Atlantic(grid, m+i, n+j, x, y, visited)
                else:
                    if not visited[m+i][n+j] and grid[m][n] >= grid[m+i][n+j]:
                        ans = ans or Atlantic(grid, m+i, n+j, x, y, visited)
            return ans
        
        ans = []
        x, y = len(heights), len(heights[0])
        for m in range(x):
            for n in range(y):
                visited = [[0] * y for _ in range(x)]
                p = Pacisic(heights, m, n, x, y, visited)
                visited = [[0] * y for _ in range(x)]
                A = Atlantic(heights, m, n, x, y, visited)
                if p and A:
                    ans.append([m, n])
        return ans
        
        
            

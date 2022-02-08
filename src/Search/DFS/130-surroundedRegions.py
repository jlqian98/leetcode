class Solution(object):
    def solve(self, board):
        """
        给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
        解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        x, y = len(board), len(board[0])
        visited = [[0] * y for _ in range(x)]
        def dfs(grid, m, n, x, y):
            if m < 0 or n < 0 or m >= x or n >= y or grid[m][n] == 'X' or visited[m][n]:
                return
            grid[m][n] = '*'
            visited[m][n] = 1
            for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dfs(grid, m+i, n+j, x, y)
        
        for m in range(x):
            for n in range(y):
                if m == 0 or n == 0 or m == x-1 or n == y-1:
                    dfs(board, m, n, x, y)

        for m in range(x):
            for n in range(y):
                if board[m][n] == '*':
                    board[m][n] = 'O'
                else:
                    board[m][n] = 'X'

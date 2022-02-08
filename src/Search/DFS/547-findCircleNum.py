class Solution(object):
    def dfs(self, x, visited, isConnected):
        if visited[x]:
            return
        visited[x] = 1
        for i in range(len(isConnected)):
            if i == x or not isConnected[i][x]:
                continue
            self.dfs(i, visited, isConnected)

    def findCircleNum(self, isConnected):
        """
        有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

        省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
        给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
        返回矩阵中 省份 的数量。
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        if n == 1:
            return 1
        visited = [0] * n
        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += 1
            self.dfs(i, visited, isConnected)

        return ans


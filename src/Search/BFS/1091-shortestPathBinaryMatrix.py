from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        if len(grid) == 1:
            return 1
            
        length = len(grid)
        direct = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]

        visited = [[0]*length for _ in range(length)]

        q = deque() # 当前要访问的节点队列
        q.appendleft([0, 0])

        # 访问初始节点
        step = 1
        visited[0][0]=1

        while q:
            step += 1
            for _ in range(len(q)):
                i, j = q.pop()      # 当前要访问的节点
                for m, n in direct:     # 枚举邻居
                    a, b = m + i, n + j
                    if 0<=a<length and 0<=b<length and visited[a][b]==0 and grid[a][b] == 0:    # 合法邻居
                        if a == length-1 and b == length-1:
                            return step
                        q.appendleft([a, b])    # 合法邻居进下一个访问队列
                        visited[a][b] = 1       # 邻居设为已访问
        return -1

        


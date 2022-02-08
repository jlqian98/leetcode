class Solution(object):
    def numSquares(self, n):
        """
        给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
        把所有数字当作一张图的所有节点，两个数字差一个完全平方数即可连成边，题目的要求即为求n到0的最短路径。  -->采用BFS求解最短路径。
        :type n: int
        :rtype: int
        """
        q = [n]
        visited = [0] * (n+1)
        visited[n] = 1
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                num = q.pop(0)
                for i in range(1, int(sqrt(num))+1):
                    neighbor = num - i*i
                    if visited[neighbor]:
                        continue
                    if neighbor == 0:
                        return ans
                    visited[neighbor] = 1
                    q.append(neighbor)
        
        return -1

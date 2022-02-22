class Solution(object):
    def findLongestChain(self, pairs):
        """
        给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。

        现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
        给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[0])
        n = len(pairs)
        dp = [0] * n
        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
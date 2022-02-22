class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
        注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        n = len(s)

        word_map = {}
        for word in wordDict:
            word_map[word] = True

        dp = [0] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            dp[i] = False
            for j in range(i):
                word = s[j:i]
                if word in word_map:
                    dp[i] = dp[j] or dp[i]

        return dp[n]
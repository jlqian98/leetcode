class Solution(object):
    def validPalindrome(self, s):
        """
        给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        flag = False
        while s[i] == s[j] and i < j:
            i += 1
            j -= 1
        if i >= j:
            return True
        x, y = i, j
        i, j = x+1, y
        while s[i] == s[j] and i < j:
            i += 1
            j -= 1
        if i >= j:
            return True
        i, j = x, y-1
        while s[i] == s[j] and i < j:
            i += 1
            j -= 1
        if i >= j:
            return True
            
        return False
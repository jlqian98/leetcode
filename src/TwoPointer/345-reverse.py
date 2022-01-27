class Solution(object):
    def reverseVowels(self, s):
        """
        给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
        元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 0
        j = len(s) - 1
        while i < j:
            while s[i] not in vowel_list and i < j:
                i += 1
            while s[j] not in vowel_list and j > i:
                j -= 1
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1

        return ''.join(s)
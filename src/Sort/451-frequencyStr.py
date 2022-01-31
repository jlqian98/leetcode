class Solution(object):
    def frequencySort(self, s):
        """
        给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
        :type s: str
        :rtype: str
        """
        char_map = {}
        for c in s:
            if c not in char_map:
                char_map[c] = 0
            char_map[c] += 1
        char_map = sorted(char_map.items(), key=lambda x: x[1], reverse=True)
        rst = ""
        for key, value in char_map:
            rst += key * value
        return rst
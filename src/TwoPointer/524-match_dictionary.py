class Solution(object):
    
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """

        def compare(a, b):
            if len(a) != len(b):
                return len(a) > len(b)
            return a < b

        ans = ""
        for word in dictionary:
            p, q = 0, 0
            while p < len(s) and q < len(word):
                if s[p] == word[q]:
                    q += 1
                p += 1
            if q == len(word) and compare(word, ans):
                ans = word
        return ans
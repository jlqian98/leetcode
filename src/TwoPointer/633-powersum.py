class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        j = 100000
        while i <= j:
            if i * i + j * j == c:
                return True
            elif i * i + j * j < c:
                i += 1
            else:
                j -= 1
        return False
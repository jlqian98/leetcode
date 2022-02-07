class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
        :type expression: str
        :rtype: List[int]
        """
        if expression.isdigit():
            return [int(expression)]
        
        ans = []
        for i, char in enumerate(expression):
            if char in ['*', '+', '-']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if char == '+':
                            ans.append(l + r)
                        elif char == '-':
                            ans.append(l - r)
                        else:
                            ans.append(l * r)
        return ans
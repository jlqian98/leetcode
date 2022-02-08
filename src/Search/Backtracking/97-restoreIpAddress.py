class Solution(object):
    def restoreIpAddresses(self, s):
        """
        有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

        例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
        给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你不能重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []
        def legal_num(num, size):
            if size == 3:
                return 100 <= num <= 255
            elif size == 2:
                return 10 <= num <= 99
            else:
                return 0 <= num <= 9

        def dfs(cur, s, idx, ans):
            if len(cur) == 4 and idx == len(s):
                ans.append(".".join(cur))
            if idx >= len(s):
                return
            for i in range(1, 4):
                if not legal_num(int(s[idx: idx+i]), i):
                    continue
                cur.append(s[idx: idx+i])
                dfs(cur, s, idx+i, ans)
                del cur[-1]
        ans = []
        cur = []
        dfs(cur, s, 0, ans)
        return ans
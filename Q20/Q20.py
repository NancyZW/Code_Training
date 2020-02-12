# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        dot = 0
        alpha = 0
        symbol = 0
        if len(s) == 0:
            return False
        if len(s) == 1:
            return str.isdigit()
        if not s[-1].isdigit():
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        for i in range(len(s)):
            str = s[i]
            if str.isdigit():
                continue
            elif str == 'e' or str == 'E':
                if alpha == 0:
                    alpha = 1
                else:
                    return False
            elif str == '.':
                if dot == 0:
                    dot = 1
                else:
                    return False
                if alpha == 1:
                    return False
            elif str == '-' or str == '+':
                if i == 0:
                    return False
                if s[i-1] !='e' and s[i-1] != 'E':
                    return False
            else:
                return False
        return True

if __name__ == "__main__":
    s = ".4"
    sol = Solution()
    ans = sol.isNumeric(s)
    print(ans)
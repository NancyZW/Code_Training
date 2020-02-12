# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        return self.whetherMatch(s,pattern)

    def whetherMatch(self, s, pattern):
        # print(s,pattern)
        if len(pattern) == 0 and len(s) != 0:
            return False
        if len(pattern) == 0 and len(s) == 0:
            return True
        if len(s) == 0:
            if pattern[-1] == '.':
                return False
            elif pattern[-1] == '*':
                return self.whetherMatch(s,pattern[0:-2])
            else:
                return False
        if pattern[-1] == '*':
            return self.whetherMatch(s,pattern[0:-2]) or self.whetherMatch(s,pattern+pattern[-2])
        elif pattern[-1] == '.':
            return self.whetherMatch(s[0:-1],pattern[0:-1])
        elif pattern[-1] == s[-1]:
            return self.whetherMatch(s[0:-1],pattern[0:-1])
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    s = "aaa"
    pattern = "ab*a"
    ans = sol.match(s, pattern)
    print(ans)
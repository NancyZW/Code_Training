# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dict = {}
        for i in s:
            x = ord(i)
            dict[x] = dict.get(x,0) + 1
        for i in range(len(s)):
            if dict[ord(s[i])] == 1:
                return i
        return -1

if __name__ == "__main__":
    n = 'google'
    sol = Solution()
    ans = sol.FirstNotRepeatingChar(n)
    print(ans)




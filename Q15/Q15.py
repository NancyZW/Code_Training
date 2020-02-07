# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if bin(n)[0]=='-':
            n += 2**32
            str_n = bin(n)[2:]
        else:
            str_n = bin(n)[2:]
        # print(bin(n))
        ans = 0
        for i in str_n:
            if i == "1":
                ans += 1
        return ans

    def NumberOf1v2(self, n):
        # write code here
        ans = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            ans += 1
            n = n&(n-1)
        return ans

n = -2
print(Solution().NumberOf1v2(n))
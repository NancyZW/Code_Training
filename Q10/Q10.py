# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            f0 = 0
            f1 = 1
            for i in range(2,n+1):
                f = f0 + f1
                f0 = f1
                f1 = f
            return f

ans = Solution().Fibonacci(5)
print(ans)

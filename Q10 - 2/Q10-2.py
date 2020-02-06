# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        n = number
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 2
        else:
            f0 = 1
            f1 = 2
            for i in range(3,n+1):
                f = f0 + f1
                f0 = f1
                f1 = f
            return f

ans = Solution().jumpFloor(3)
print(ans)

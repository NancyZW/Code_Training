# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        n = number
        f = [0,1]
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            for i in range(2,n+1):
                fi = 0
                for j in range(i):
                    fi += f[j]
                    # print(f[j])
                f.append(fi+1)
            return f[n]

ans = Solution().jumpFloor(3)
print(ans)

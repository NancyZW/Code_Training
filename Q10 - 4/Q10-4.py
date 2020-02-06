# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        n = number
        f = [0,1,2]
        for i in range(2,n+1):
            fi = f[-1]+f[-2]
            f.append(fi)
        return f[n]

ans = Solution().rectCover(4)
print(ans)

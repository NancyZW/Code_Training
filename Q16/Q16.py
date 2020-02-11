# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if base == 0:
            return 0
        if exponent < 0:
            base = 1/base
            exponent = -exponent
        ans = 1
        for i in range(exponent):
            ans = base*ans
        return ans

if __name__ == "__main__":
    base = 4
    exponent = -1
    sol = Solution()
    ans = sol.Power(base,exponent)
    print(ans)
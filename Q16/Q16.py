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
    def Power2(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        if exponent < 0:
            base = 1/base
            exponent = -exponent
        if exponent & 1 == 1:
            ans = self.Power2(base, exponent>>1) * self.Power2(base, exponent>>1)*base
        else:
            ans = self.Power2(base,exponent>>1)*self.Power2(base,exponent>>1)
        return ans




if __name__ == "__main__":
    base = 4
    exponent = -1
    sol = Solution()
    ans = sol.Power(base,exponent)
    ans = sol.Power2(base,exponent)
    print(ans)
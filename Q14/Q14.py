# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        ans = 0
        for i in range(2, number+1):
            ans = max(ans, self.SubcutRop(number,i))
        return ans

    def SubcutRop(self, n, m):
        res = 1
        while m>=1:
            k0 = int(n/m)
            m -= 1
            n -= k0
            res *= k0
        return res

    def cutRope2(self, number):
        # print(number)
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 1
        elif number == 3:
            return 2
        else:
            return self.SubcutRop2(number)

    def SubcutRop2(self, number):
        final = 0
        for i in range(1, number):
            ans = i * self.SubcutRop2(number - i)
            final = max(final, ans)
        return max(final, number)

number = 8
ans = Solution().cutRope2(number)
print(ans)